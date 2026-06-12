potential_customers = ["소비자A", "소비자B", "소비자C", "소비자D", "소비자E"]
product_known = False  # 신제품 인지 여부
total_sales = 0        # 총 판매량

print("🚀 신제품 마케팅 및 판매 시뮬레이션을 시작합니다.")
print("-" * 50)

# 1. 반복문 (for문): 잠재 고객들을 한 명씩 만나는 과정
for customer in potential_customers:
    print(f"\n[안내] {customer}님에게 다가갑니다.")
    
    # 가상의 시나리오: 소비자A와 C는 이미 광고를 봤고, 나머지는 모르는 상태
    if customer in ["소비자A", "소비자C"]:
        product_known = True
    else:
        product_known = False
        
    # 2. 조건문 (if-elif-else문): 인지 여부에 따른 마케팅 행동 및 판매 판단
    if product_known == True:
        # 제품을 아는 경우 -> 바로 구매 유도
        print(f" {customer}님은 이미 신제품을 알고 계십니다! -> 🛒 제품 구매 완료!")
        total_sales += 1
    else:
        # 제품을 모르는 경우 -> 홍보 진행 후 구매 결정
        print(f" {customer}님은 신제품을 잘 모릅니다. -> 📢 무료 체험단 및 SNS 홍보 진행!")
        
        # 홍보 후 구매할 확률 (여기서는 예시로 무조건 구매한다고 가정)
        print(f" 홍보 효과로 인해 {customer}님이 제품을 인지하고 -> 🛒 제품 구매 완료!")
        total_sales += 1

# 3. 결과 출력
print("-" * 50)
print(f"📊 시뮬레이션 종료 | 총 판매량: {total_sales}개")
print("💡 결론: 알지 못하는 소비자에게 홍보(조건문 처리)를 진행하여 판매량을 높였습니다!")
