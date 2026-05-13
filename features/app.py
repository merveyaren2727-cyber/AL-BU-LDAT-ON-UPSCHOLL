import html
import io
import os
import tempfile
import streamlit as st
from fpdf import FPDF
from pptx import Presentation
import google.generativeai as genai

try:
    import pandas as pd
except ImportError:
    pd = None

try:
    from PIL import Image
except ImportError:
    Image = None

# --- AI YAPILANDIRMASI (ORTA SEVİYE DOKUNUŞ) ---
genai.configure(api_key="AIzaSyD5yoDFLTl5iV8_TIx5MKWi7E6O6uOnGJA")
model = genai.GenerativeModel(
    model_name='gemini-1.5-flash',
    system_instruction="Sen Bridge-AI asistanısın. Sevde Nisa tarafından geliştirildin. Eğitim içeriklerinde 11. sınıf seviyesine uygun, yaratıcı ve samimi bir dil kullan."
)

def get_ai_analysis(prompt, file_uploader_key):
    upl = st.session_state.get(file_uploader_key)
    if upl:
        try:
            img = Image.open(upl)
            response = model.generate_content([prompt, img])
            return response.text
        except Exception as e:
            return f"Analiz Hatası: {str(e)}"
    return "Lütfen önce bir dosya yükleyin."

# --- 1. PDF MOTORU (HATA GİDERİLDİ) ---
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
    slide.shapes.title.text = "Bridge-AI Analiz Çıktısı"
    slide.placeholders[1].text = slide_text[:500]
    output = io.BytesIO()
    prs.save(output)
    return output.getvalue()

def render_preview(placeholder, body_inner_html: str):
    placeholder.markdown(
        '<div class="preview-container preview-flex"><div class="preview-body-col">'
        + body_inner_html + "</div>"
        + f'<div class="preview-notes-col"><strong>Bridge-AI Notu</strong><p style="margin:0;">{st.session_state.get("ai_msg", "İşlem yapıldığında AI notları burada görünür.")}</p></div>'
        + "</div>",
        unsafe_allow_html=True,
    )

def go_rerun(celebrate: bool = False):
    if celebrate: st.session_state["celebrate"] = True
    st.rerun()

# --- 2. TASARIM VE CSS ---
st.set_page_config(page_title="BRIDGE-AI® Enterprise PRO", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    [data-testid="stSidebar"] { background-color: #001f3f !important; }
    [data-testid="stSidebar"] * { color: white !important; font-weight: 600; }
    .kpi-container { display: flex; justify-content: space-between; gap: 10px; margin-bottom: 20px; }
    .kpi-card { background-color: white; padding: 15px 25px; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); flex: 1; border: 1px solid #e2e8f0; }
    .preview-container { border: 2px dashed #10B981 !important; border-radius: 15px; background-color: #ffffff; min-height: 450px; padding: 22px; display: flex; gap: 18px; }
    .preview-body-col { flex: 1.55; }
    .preview-notes-col { flex: 1; border-left: 3px dashed #10B981; padding-left: 16px; color: #0f172a; }
    .paper-mockup { background-color: white; border: 1px solid #e2e8f0; padding: 30px; box-shadow: 0 10px 25px rgba(0,0,0,0.1); font-family: 'serif'; text-align: left; color: #1e293b; width: 100%; }
    .op-card { background-color: white; padding: 25px; border-radius: 12px; border: 1px solid #e2e8f0; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR ---
with st.sidebar:
    st.title("BRIDGE-AI®")
    module = st.radio("NAVİGASYON", ["Eğitim & Akademi", "Saha (Field)", "Ofis & İdari İşler"])
    st.write(f"👤 Sevde Nisa")
    
    st.divider()
    st.subheader("🚀 Gelişim Yol Haritası")
    with st.expander("🟢 Başlangıç (Şu An)", expanded=True):
        st.info("- Gemini 1.5 Entegrasyonu\n- Sistem Mesajı Analizi\n- Multimodal Analiz")

# --- 4. ÜST PANEL ---
st.markdown(f"""
    <div class="kpi-container">
        <div class="kpi-card"><span>TOTAL ANALYSES</span><strong>DYNAMIC AI</strong></div>
        <div class="kpi-card"><span>STATUS</span><strong style="color:#10B981">LIVE 🟢</strong></div>
        <div class="kpi-card"><span>ENGINE</span><strong>GEMINI 1.5 FLASH</strong></div>
        <div class="kpi-card"><span>VERSION</span><strong>2.0 PRO</strong></div>
    </div>
""", unsafe_allow_html=True)

st.header(f"📊 {module} Kontrol Paneli")

# --- 5. ANA PANEL ---
col_left, col_right = st.columns([2.3, 1])

with col_left:
    preview_placeholder = st.empty()
    state = st.session_state.get("view_state")

    if not state:
        render_preview(preview_placeholder, '<div style="text-align:center;padding:40px;color:#64748b;">📂 Analiz için dosya yükleyip butonlara basın.</div>')
    else:
        ai_content = st.session_state.get('ai_msg', "Veri yok.")
        if state == "pdf":
            render_preview(preview_placeholder, f'<div class="paper-mockup"><center><h3>SINAV ANALİZ ÇIKTISI</h3></center><hr><div style="white-space: pre-wrap;">{html.escape(ai_content)}</div></div>')
            st.download_button("📥 Sınavı PDF İndir", create_general_pdf("SINAV ANALİZİ", ai_content), "sinav.pdf", "application/pdf", use_container_width=True)
        elif state == "slide":
            render_preview(preview_placeholder, f'<div style="background:#001f3f;color:white;padding:40px;border-radius:10px;width:100%;border-left:12px solid #10B981;"><h3>SUNUM TASLAĞI</h3><hr><div style="white-space: pre-wrap;">{html.escape(ai_content)}</div></div>')
            st.download_button("📥 Sunumu İndir (.pptx)", create_presentation_pptx("SUNUM TASLAĞI", ai_content), "sunum.pptx", use_container_width=True)
        elif state == "vocab":
            render_preview(preview_placeholder, f'<div class="paper-mockup"><h3>🎓 KELİME BANKASI VE ÖZET</h3><hr><div style="white-space: pre-wrap;">{html.escape(ai_content)}</div></div>')
            st.download_button("📥 Özeti PDF İndir", create_general_pdf("KELİME BANKASI", ai_content), "ozet.pdf", "application/pdf", use_container_width=True)

    st.markdown('<div class="op-card">', unsafe_allow_html=True)
    if module == "Eğitim & Akademi":
        upl = st.file_uploader("Ders Materyali Yükle", type=['pdf', 'png', 'jpg', 'jpeg'], key="edu_u")
        b1, b2, b3 = st.columns(3)
        if b1.button("✨ Sunum Hazırla", use_container_width=True) and upl:
            with st.spinner("AI hazırlanıyor..."):
                res = get_ai_analysis("Bu görseli profesyonel bir sunum taslağı haline getir.", "edu_u")
                st.session_state.update({"ai_msg": res, "view_state": "slide"})
                go_rerun(True)
        if b2.button("📄 Sınav Üret", use_container_width=True):
            st.session_state['show_slider'] = True
        if b3.button("🎓 Kelime Bankası", use_container_width=True) and upl:
            with st.spinner("AI analiz ediyor..."):
                res = get_ai_analysis("Bu görseldeki anahtar kelimeleri ve konuyu özetle.", "edu_u")
                st.session_state.update({"ai_msg": res, "view_state": "vocab"})
                go_rerun(True)
        
        if st.session_state.get('show_slider'):
            cnt = st.select_slider("Soru Sayısı", options=[5, 10, 15], value=5)
            if st.button("Kutuda Sınavı Oluştur", use_container_width=True) and upl:
                with st.spinner(f"{cnt} soru hazırlanıyor..."):
                    res = get_ai_analysis(f"Bu görselle ilgili {cnt} adet test sorusu ve cevap anahtarı hazırla.", "edu_u")
                    st.session_state.update({"ai_msg": res, "view_state": "pdf"})
                    go_rerun(True)

    elif module == "Saha (Field)":
        upl = st.file_uploader("Saha Fotoğrafı Yükle", type=['png', 'jpg', 'jpeg'], key="field_u")
        if st.button("🔍 İSG & 5S Analizi", use_container_width=True) and upl:
            with st.spinner("Saha denetleniyor..."):
                res = get_ai_analysis("Bu saha fotoğrafını İSG ve 5S açısından denetle, riskleri listele.", "field_u")
                st.session_state.update({"ai_msg": res, "view_state": "pdf"})
                go_rerun(True)
    st.markdown('</div>', unsafe_allow_html=True)

with col_right:
    st.markdown('<div class="op-card" style="border-left: 5px solid #10B981; min-height:550px;">', unsafe_allow_html=True)
    st.subheader("💡 BRIDGE-AI®")
    st.info("Bu sistem Gemini 1.5 Flash ile fotoğraflarınızı anlık analiz eder.")
    if st.button("🗑️ Hafızayı Temizle"):
        st.session_state.clear()
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

if st.session_state.get("celebrate"):
    st.balloons()
    st.session_state.pop("celebrate", None)
