import streamlit as st
import math

# Cấu hình trang web
st.set_page_config(page_title="Tính Viền Ngành May", page_icon="✂️", layout="centered")

st.title("✂️ Phần Mềm Tính Viền Chuyên Nghiệp")
st.markdown("---")

# Tạo 2 Tab
tab1, tab2 = st.tabs(["📏 Tính Vải Cần Mua (Chuẩn)", "🧵 Tính Vải Cần Mua (Tiết Kiệm)"])

# ==========================================
# TAB 1: TÍNH VẢI CHUẨN
# ==========================================
with tab1:
    st.subheader("Thông số đầu vào")
    
    col_dv1, col_loai1 = st.columns(2)
    with col_dv1:
        donvi1 = st.selectbox("Đơn vị tính", ["CM", "INCH"], key="dv1")
    with col_loai1:
        loai_vien1 = st.selectbox("Kiểu cắt viền", ["Viền Xéo", "Viền Ngang", "Viền Dọc"], key="lv1")
        
    dv_txt = donvi1.lower()
    
    col1, col2 = st.columns(2)
    with col1:
        sl1 = st.number_input("Số lượng sản phẩm (SL)", min_value=1.0, value=100.0, step=1.0)
        s1 = st.number_input(f"Khổ vải ({dv_txt})", min_value=1.0, value=100.0, step=1.0)
        w1 = st.number_input(f"To bản viền ({dv_txt})", min_value=0.1, value=3.0, step=0.1)
        
    with col2:
        csp1 = st.number_input(f"Chiều dài viền/SP ({dv_txt})", min_value=1.0, value=50.0, step=1.0)
        
        if loai_vien1 == "Viền Xéo":
            cr1 = st.number_input("Độ co giãn dây viền (CR)", value=0.0, step=0.1)
            khuc1 = st.number_input("Số khúc vải", min_value=1, value=1, step=1)
        else:
            cr1, khuc1 = 0, 1 # Giá trị mặc định khi ẩn

    if st.button("TÍNH TOÁN VẢI CHUẨN", type="primary", use_container_width=True):
        Chieu_dai_can_mua = 0
        try:
            if loai_vien1 == "Viền Xéo":
                l = w1 / math.sin(math.radians(45))
                DC1 = ((s1 * math.sqrt(2)) - w1) + cr1
                so_vien_1_duong = int(DC1 / csp1)
                
                if so_vien_1_duong > 0:
                    L1 = (l * (sl1 / so_vien_1_duong)) + s1
                    tong_so_soi_1_tam_giac = 0
                    i = 1
                    while True:
                        dc2 = (s1 - i * l) * math.sqrt(2) + cr1
                        if dc2 < csp1: break
                        tong_so_soi_1_tam_giac += int(dc2 / csp1)
                        i += 1
                        if i > 1000: break
                    
                    he_so_tam_giac = 2 if khuc1 == 1 else khuc1 - 1
                    tong_so_soi_tru = tong_so_soi_1_tam_giac * he_so_tam_giac
                    so_lan_tru = int(tong_so_soi_tru / so_vien_1_duong)
                    L2_tru = so_lan_tru * l
                    Chieu_dai_can_mua = L1 - L2_tru
                else:
                    st.error("Đường chéo 1 (DC1) nhỏ hơn chiều dài 1 SP!")
                    
            elif loai_vien1 == "Viền Ngang":
                so_sp_1_soi = int(s1 / csp1)
                if so_sp_1_soi > 0:
                    so_soi_ngang = math.ceil(sl1 / so_sp_1_soi)
                    Chieu_dai_can_mua = so_soi_ngang * w1
                else:
                    st.error("Khổ vải nhỏ hơn chiều dài 1 SP!")
                    
            elif loai_vien1 == "Viền Dọc":
                so_soi_doc = int(s1 / w1)
                if so_soi_doc > 0:
                    so_lan_chieu_dai = math.ceil(sl1 / so_soi_doc)
                    Chieu_dai_can_mua = so_lan_chieu_dai * csp1
                else:
                    st.error("To bản viền lớn hơn khổ vải!")

            if Chieu_dai_can_mua > 0:
                val = Chieu_dai_can_mua / 100 if donvi1 == "CM" else Chieu_dai_can_mua / 36
                unit = "M" if donvi1 == "CM" else "YARDS"
                st.success(f"### CHIỀU DÀI VẢI CẦN MUA: {val:g} {unit}")
        except Exception as e:
            st.error("Vui lòng kiểm tra lại thông số nhập vào.")


# ==========================================
# TAB 2: TÍNH VẢI TIẾT KIỆM
# ==========================================
with tab2:
    st.subheader("Thông số đầu vào")
    
    col_dv2, col_loai2 = st.columns(2)
    with col_dv2:
        donvi2 = st.selectbox("Đơn vị tính", ["CM", "INCH"], key="dv2")
    with col_loai2:
        loai_vien2 = st.selectbox("Kiểu cắt viền", ["Viền Xéo", "Viền Ngang", "Viền Dọc"], key="lv2")
        
    dv_txt2 = donvi2.lower()
    
    col3, col4 = st.columns(2)
    with col3:
        sl2 = st.number_input("Số lượng sản phẩm (SL)", min_value=1.0, value=100.0, step=1.0, key="sl2")
        s2 = st.number_input(f"Khổ vải ({dv_txt2})", min_value=1.0, value=100.0, step=1.0, key="s2")
        w2 = st.number_input(f"To bản viền ({dv_txt2})", min_value=0.1, value=3.0, step=0.1, key="w2")
        
    with col4:
        csp2 = st.number_input(f"Chiều dài viền/SP ({dv_txt2})", min_value=1.0, value=50.0, step=1.0, key="csp2")
        
        if loai_vien2 == "Viền Xéo":
            cr2 = st.number_input("Độ co giãn dây viền (CR)", value=0.0, step=0.1, key="cr2")
            ghv2 = st.number_input(f"Giới hạn dây viền ({dv_txt2})", value=30.0, step=1.0, key="ghv2")
            khuc2 = st.number_input("Số khúc vải", min_value=1, value=1, step=1, key="khuc2")
        else:
            cr2, ghv2, khuc2 = 0, 30, 1

    if st.button("TÍNH TOÁN VẢI TIẾT KIỆM", type="primary", use_container_width=True, key="btn2"):
        hs = 1 if donvi2 == "CM" else (1 / 2.54)
        L_req = sl2 * csp2
        Lv_cm = 0
        
        try:
            if loai_vien2 == "Viền Xéo":
                l = w2 / math.sin(math.radians(45))
                sum_dc2 = 0
                count_soi = 0
                i = 1
                while True:
                    dc2 = (s2 - i * l) * math.sqrt(2) + cr2
                    if dc2 < ghv2: break
                    sum_dc2 += dc2
                    count_soi += 1
                    i += 1
                    if i > 1000: break
                
                chieu_dai_1_tg = sum_dc2 + (count_soi - 1) * w2 - (2 * hs * (count_soi - 1)) if count_soi > 0 else 0
                so_tam_giac = khuc2 + 1 
                tong_chieu_dai_tam_giac = chieu_dai_1_tg * so_tam_giac
                
                L_rect_req = L_req - tong_chieu_dai_tam_giac
                if L_rect_req < 0: L_rect_req = 0
                
                DC1 = (s2 * math.sqrt(2)) - w2 + cr2
                if DC1 > 0:
                    n_soi = math.ceil(L_rect_req / DC1) if L_rect_req > 0 else 0
                    Lv_cm = (n_soi * l) + s2
                else:
                    st.error("Thông số không hợp lệ để tạo đường chéo!")
                    
            elif loai_vien2 == "Viền Ngang":
                E_ngang = s2 - (2 * hs)
                if E_ngang > 0:
                    n_soi = math.ceil(L_req / E_ngang)
                    Lv_cm = n_soi * w2
                else:
                    st.error("Khổ vải quá nhỏ so với phần hao hụt nối!")
                    
            elif loai_vien2 == "Viền Dọc":
                n_soi = int(s2 / w2)
                if n_soi > 0:
                    Lv_cm = (L_req / n_soi) + (2 * hs)
                else:
                    st.error("To bản viền lớn hơn khổ vải!")

            if Lv_cm > 0:
                val = Lv_cm / 100 if donvi2 == "CM" else Lv_cm / 36
                unit = "M" if donvi2 == "CM" else "YARDS"
                st.success(f"### CHIỀU DÀI VẢI CẦN MUA: {val:g} {unit}")
        except Exception as e:
            st.error("Vui lòng kiểm tra lại thông số nhập vào.")
