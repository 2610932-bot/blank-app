import streamlit as st

# 1. 앱 페이지 레이아웃 및 제목 설정
st.set_page_config(page_title="신제품 마케팅 대시보드", layout="centered")
st.title("📢 신제품 인지도 및 판매량 분석 시스템")
st.write("소비자들이 신제품을 잘 알지 못해 판매량이 낮은 문제를 해결하기 위한 시뮬레이션입니다.")
st.divider()

# 2. 필수 초기 세팅 데이터
products = ["신제품A", "신제품B", "신제품C"]
ads = [1000, 2000, 3000]

# 조건문 기준점 및 결과 저장용 변수 초기화
known_list = []  # 소비자가 알게 된 제품을 담을 빈 리스트
total_sales = 0  # 총 판매량

# 3. 사이드바 - 대화형 광고비 조절 UI (반복문 활용)
st.sidebar.header("⚙️ 제품별 광고비 설정")
st.sidebar.write("광고비를 움직여 소비자의 인지도를 높여보세요.")

updated_ads = []
for product, default_ad in zip(products, ads):
    # 사용자가 직접 조절하는 슬라이더
    ad_input = st.sidebar.slider(f"{product} 광고비 (만원)", 0, 5000, default_ad, step=500)
    updated_ads.append(ad_input)

# 4. 메인 화면 - 반복문과 조건문을 통한 실시간 진단
st.subheader("🔍 실시간 제품별 시장 반응 분석")

for product, ad_budget in zip(products, updated_ads):
    
    # [조건문] 광고비가 2500만 원 미만일 때: 소비자가 잘 모름 (주제 반영)
    if ad_budget < 2500:
        st.error(f"❌ **{product}** | 현재 광고비: {ad_budget}만원")
        st.markdown("> **상태:** 홍보 부족으로 소비자가 제품을 잘 모릅니다. ➡️ **[판매량 저조]**")
    
    # [조건문] 광고비가 2500만 원 이상일 때: 소비자가 잘 알게 됨
    else:
        st.success(f"✅ **{product}** | 현재 광고비: {ad_budget}만원")
        st.markdown("> **상태:** 성공적인 홍보로 소비자들이 잘 알고 있습니다! ➡️ **[판매량 급증]**")
        
        # 소비자가 알게 된 제품이므로 known_list에 추가 (append)
        known_list.append(product)
        total_sales += 1

st.divider()

# 5. 최종 마케팅 성과 출력 (known_list 상태 시각화)
st.subheader("📊 마케팅 성과 및 데이터 적재 결과")

col1, col2 = st.columns(2)
with col1:
    st.metric(label="🛒 총 성공적 판매량", value=f"{total_sales} 개")
with col2:
    st.metric(label="💡 인지된 제품 수", value=f"{len(known_list)} 개")

# 문제의 핵심인 'known_list' 리스트 상태를 화면에 바 형태로 보여줌
st.info(f"📋 **현재 소비자가 잘 알고 있는 제품 리스트 (known_list) :** {known_list}")

# 모든 제품을 소비자가 알게 되었을 때의 보너스 연출
if len(known_list) == len(products):
    st.balloons()
    st.success("🎉 모든 신제품의 인지도 부족 문제를 해결하여 판매량을 극대화했습니다!")
else:
    st.warning("💡 **분석 조치:** `known_list`에 포함되지 못한 제품은 소비자가 몰라 판매량이 낮습니다. 왼쪽 사이드바에서 광고비를 더 올려보세요!")