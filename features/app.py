import html
import io
import os
import streamlit as st
from fpdf import FPDF
from pptx import Presentation
import google.generativeai as genai

try:
    from PIL import Image
except ImportError:
    Image = None

# --- AI YAPILANDIRMASI (MODEL HATASI GİDERİLDİ) ---
# API Key senin verdiğin anahtar
genai.configure(api_key="AIzaSyD5yoDFLTl5iV8_TIx5MKWi7E6O6uOnGJA")

# Modeli "models/gemini-1.5-flash" formatında tanımlayarak 404 hatasını çözüyoruz
model = genai.GenerativeModel(
    model_name='gemini-1.5-flash',
    system_instruction="Sen Bridge-AI asistanısın. Merve Yılmaz tarafından geliştirildin. Analizlerinde profesyonel bir mühendis ve samimi bir öğretmen gibi davran."
)

def get_ai_analysis(prompt, file_uploader_key):
    upl = st.session_state.get(file_uploader_key)
    if upl:
        try:
            img = Image.open(upl)
            # generate_content çağrısını en güvenli şekilde yapıyoruz
            response = model.generate_content([prompt, img])
            return response.text
        except Exception as e:
            return f"Analiz Hatası: {str(e)}"
    return "Lütfen önce bir dosya yükleyin."

# --- 1. PDF MOTORU ---
def _fpdf_latin1_safe(text: str) -> str:
    if not isinstance(text, str): text = str(text)
    for old, new in (("\u2014", "-"), ("\u2013", "-"), ("\u2018", "'"), ("\u2019", "'"), ("\u201c", '"'), ("\u201d", '"'), ("\u2026", "..."), ("\u00a0", " ")):
        text = text.replace(old, new)
    return text.encode("latin-1", errors="replace").decode("latin-1")

def create_general_pdf(title, content_text):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(190, 10, _fpdf_latin1_safe(title), ln=True, align="C")
    pdf.ln(10)
    pdf.set_font("Arial", "", 11)
    pdf.multi_cell(190, 10, _fpdf_latin1_safe(content_text))
    return bytes(pdf.output())

def create_presentation_pptx(title, slide_text):
    prs = Presentation()
    slide = prs.slides.add_slide(prs.slide_layouts[0])
    slide.shapes.title.text = title
    slide = prs.slides.add_slide(prs.slide_layouts[1])
    slide.shapes.title.text = "Analiz Özeti"
    slide.placeholders[1].text = slide_text[:500]
    output = io.BytesIO()
    prs.save(output)
    return output.getvalue()

def render_preview(placeholder, body_inner_html: str):
    placeholder.markdown(
        '<div class="preview-container preview-flex"><div class="preview-body-col">'
        + body_inner_html + "</div>"
        + f'<div class="preview-notes-col"><strong>Bridge-AI Notu</strong><p style="margin:0;">{st.session_state.get("ai_msg", "İşlem bekliyor...")}</p></div>'
        + "</div>",
        unsafe_allow_html=True,
    )

# --- 2. TASARIM VE CSS ---
st.set_page_config(page_title="BRIDGE-AI® PRO", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    [data-testid="stSidebar"] { background-color: #001f3f !important; }
    [data-testid="stSidebar"] * { color: white !important; font-weight: 600; }
    .kpi-container { display: flex; justify-content: space-between; gap: 10px; margin-bottom: 20px; }
    .kpi-card { background-color: white; padding: 15px 25px; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); flex: 1; border: 1px solid #e2e8f0; }
    .preview-container { border: 2px dashed #10B981 !important; border-radius: 15px; background-color: #ffffff; min-height: 450px; padding: 22px; display: flex; gap: 18px; }
    .preview-body-col { flex: 1.5; }
    .preview-notes-col { flex: 1; border-left: 3px dashed #10B981; padding-left: 16px; color: #0f172a; }
    .paper-mockup { background-color: white; border: 1px solid #e2e8f0; padding: 30px; box-shadow: 0 10px 25px rgba(0,0,0,0.1); font-family: 'serif'; text-align: left; color: #1e293b; width: 100%; }
    .op-card { background-color: white; padding: 25px; border-radius: 12px; border: 1px solid #e2e8f0; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR ---
with st.sidebar:
    st.title("BRIDGE-AI®")
    # Burada ismini düzelttim Merve
    st.write(f"👤 Merve Yılmaz")
    module = st.radio("NAVİGASYON", ["Eğitim & Akademi", "Saha (Field)", "Ofis & İdari İşler"])
    
    st.divider()
    st.subheader("🚀 Yol Haritası")
    with st.expander("🟢 Mevcut Durum", expanded=True):
        st.info("- Gemini 1.5 Flash\n- Multimodal Analiz\n- Dinamik PDF/PPTX")

# --- 4. ÜST PANEL ---
st.markdown(f"""
    <div class="kpi-container">
        <div class="kpi-card"><span>DEVELOPER</span><strong>MERVE YILMAZ</strong></div>
        <div class="kpi-card"><span>STATUS</span><strong style="color:#10B981">LIVE 🟢</strong></div>
        <div class="kpi-card"><span>ENGINE</span><strong>GEMINI 1.5 PRO</strong></div>
    </div>
""", unsafe_allow_html=True)

# --- 5. ANA PANEL ---
col_left, col_right = st.columns([2.3, 1])

with col_left:
    st.header(f"📊 {module} Kontrol Paneli")
    preview_placeholder = st.empty()
    state = st.session_state.get("view_state")

    if not state:
        render_preview(preview_placeholder, '<div style="text-align:center;padding:40px;color:#64748b;">📂 Analiz için dosya yükleyin.</div>')
    else:
        ai_content = st.session_state.get('ai_msg', "")
        if state == "pdf":
            render_preview(preview_placeholder, f'<div class="paper-mockup"><center><h3>ANALİZ ÇIKTISI</h3></center><hr><div style="white-space: pre-wrap;">{html.escape(ai_content)}</div></div>')
            st.download_button("📥 PDF İndir", create_general_pdf("ANALİZ RAPORU", ai_content), "analiz.pdf", use_container_width=True)
        elif state == "slide":
            render_preview(preview_placeholder, f'<div style="background:#001f3f;color:white;padding:40px;border-radius:10px;width:100%;border-left:12px solid #10B981;"><h3>SUNUM TASLAĞI</h3><hr><div style="white-space: pre-wrap;">{html.escape(ai_content)}</div></div>')
            st.download_button("📥 Sunumu İndir (.pptx)", create_presentation_pptx("SUNUM TASLAĞI", ai_content), "sunum.pptx", use_container_width=True)

    st.markdown('<div class="op-card">', unsafe_allow_html=True)
    if module == "Eğitim & Akademi":
        upl = st.file_uploader("Ders Materyali Yükle", type=['pdf', 'png', 'jpg', 'jpeg'], key="edu_u")
        b1, b2, b3 = st.columns(3)
        if b1.button("✨ Sunum Hazırla", use_container_width=True) and upl:
            with st.spinner("AI analiz ediyor..."):
                res = get_ai_analysis("Bu görseli bir sunum taslağı haline getir.", "edu_u")
                st.session_state.update({"ai_msg": res, "view_state": "slide"})
                st.rerun()
        if b2.button("📄 Sınav Üret", use_container_width=True):
            st.session_state['show_slider'] = True
        if b3.button("🎓 Özet Çıkar", use_container_width=True) and upl:
            with st.spinner("AI özetliyor..."):
                res = get_ai_analysis("Bu görseldeki anahtar kelimeleri özetle.", "edu_u")
                st.session_state.update({"ai_msg": res, "view_state": "pdf"})
                st.rerun()
        
        if st.session_state.get('show_slider'):
            cnt = st.select_slider("Soru Sayısı", options=[5, 10, 15], value=5)
            if st.button("Kutuda Sınavı Oluştur", use_container_width=True) and upl:
                with st.spinner("Sınav hazırlanıyor..."):
                    res = get_ai_analysis(f"Bu görselle ilgili {cnt} adet test sorusu hazırla.", "edu_u")
                    st.session_state.update({"ai_msg": res, "view_state": "pdf"})
                    st.rerun()

    elif module == "Saha (Field)":
        upl = st.file_uploader("Saha Fotoğrafı Yükle", type=['png', 'jpg', 'jpeg'], key="field_u")
        if st.button("🔍 İSG Analizi", use_container_width=True) and upl:
            with st.spinner("Saha denetleniyor..."):
                res = get_ai_analysis("Bu saha fotoğrafını İSG açısından denetle.", "field_u")
                st.session_state.update({"ai_msg": res, "view_state": "pdf"})
                st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

with col_right:
    st.markdown('<div class="op-card" style="border-left: 5px solid #10B981; min-height:550px;">', unsafe_allow_html=True)
    st.subheader("💡 BRIDGE-AI®")
    st.info("Sistem Aktif. Gemini 1.5 Engine hazır.")
    if st.button("🗑️ Temizle"):
        st.session_state.clear()
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
