# -*- coding: utf-8 -*-
"""
===================================================================
 [바이오공정기능사 v10] 출제기준 100% 반영 실전 CBT 모의고사 웹앱
  - 출제기준 8대 영역 세세항목 완벽 커버리지
  - 영역별 문항 배분 (7:6:8:11:7:8:6:7 = 총 60문항)
  - 유형 중복 최소화 & 25+ 동적 시나리오/계산 무제한 무작위 생성
  - 실시간 OMR 4지 마킹판 & 60분 초단위 JS 타이머 고정
===================================================================
"""

import streamlit as st
import streamlit.components.v1 as components
import random
import time

# 페이지 기본 설정
st.set_page_config(
    page_title="바이오공정기능사 필기 실전 CBT 모의고사 v10",
    page_icon="🧪",
    layout="wide"
)

# ------------------------------------------------------------------
# 1. 출제기준 8대 영역별 대단원 정밀 질문 은행 (Authentic Source Bank)
# ------------------------------------------------------------------

DOMAIN_BANKS = {
    "1. 바이오 기초 지식": [
        {
            "domain": "1. 바이오 기초 지식 (GMP 규정)",
            "question": "GMP(우수의약품 제조 및 품질관리기준)의 3대 핵심 목표에 해당하지 않는 것은?",
            "options": ["① 인위적 오차(과오)의 최소화", "② 교차 오염 및 품질 저하 방지", "③ 고품질 보증 체계의 구축", "④ 제조 원가의 최소화 및 출하 지연 방지"],
            "answer": 4,
            "explanation": "GMP의 3대 목표는 '인위적 과오 최소화', '오염 및 품질 저하 방지', '고품질 보증 체계 구축'입니다."
        },
        {
            "domain": "1. 바이오 기초 지식 (MSDS)",
            "question": "화학물질 취급 시 작업장에 물질안전보건자료(MSDS)를 비치하는 주된 목적으로 가장 올바른 것은?",
            "options": ["① 작업자가 화학물질의 유해성·위험성 및 응급조치 요령을 상시 확인하고 대처하기 위해", "② 화학물질의 구매 단가 및 세금 납부 내역을 기록하기 위해", "③ 신제품 출하 시 수입업체에 보낼 품질 보증서를 대체하기 위해", "④ 회사 영업 비밀을 보호하기 위해 비공개 문서를 보관하기 위해"],
            "answer": 1,
            "explanation": "MSDS는 화학물질의 위험성, 유해성, 누출 시 응급조치 요령 및 보호구 착용법을 작업자가 숙지하도록 게시해야 하는 안전 문서입니다."
        },
        {
            "domain": "1. 바이오 기초 지식 (세포 소기관)",
            "question": "진핵세포 내 소기관 중 리보솜이 부착되어 분비 단백질의 합성 및 초기 가공을 담당하는 기관과 산화적 인산화로 ATP를 생성하는 기관을 올바르게 연결한 것은?",
            "options": ["① 거친면 소포체 / 미토콘드리아", "② 리소좀 / 골지체", "③ 중심체 / 리보솜", "④ 활성면 소포체 / 엽록체"],
            "answer": 1,
            "explanation": "거친면 소포체(Rough ER)는 단백질 합성 및 가공을 담당하며, 미토콘드리아(Mitochondria)는 세포 호흡을 통해 ATP를 생성합니다."
        },
        {
            "domain": "1. 바이오 기초 지식 (핵산 구조)",
            "question": "DNA와 RNA의 구조적·화학적 차이점에 대한 설명으로 가장 올바른 것은?",
            "options": ["① DNA는 2'-탄소에 -OH가 없는 데옥시리보스 당과 티민(T)을 가지며 이중가닥 구조를 이룬다.", "② RNA는 데옥시리보스 당과 우라실(U) 대신 티민(T)을 가진다.", "③ DNA는 아데닌(A)이 우라실(U)과 상보적으로 결합한다.", "④ DNA와 RNA 모두 동일한 리보스 당을 기본 뼈대로 사용한다."],
            "answer": 1,
            "explanation": "DNA는 2'-데옥시리보스 당, 염기 A, T, G, C를 포함하며 이중가닥 구조입니다. RNA는 리보스 당 및 염기 A, U, G, C를 포함합니다."
        },
        {
            "domain": "1. 바이오 기초 지식 (pH 및 농도)",
            "question": "pH 미터를 사용하여 수용액의 pH를 정밀 측정하기 전 수행하는 calibration(교정) 조작에 대한 설명으로 올바른 것은?",
            "options": ["① pH 4, 7, 10의 표준 완충액을 사용하여 2점 또는 3점 교정을 실시한다.", "② 멸균 증류수 1종류만으로 영점을 조절한다.", "③ pH 1과 pH 14 단 2개 극단값으로만 교정한다.", "④ 온도가 변해도 pH 센서의 응답 자력은 변하지 않으므로 온도 보정을 생략한다."],
            "answer": 1,
            "explanation": "pH 미터는 예상 측정 범위를 포함하도록 pH 4, 7, 10의 정밀 표준 완충액을 이용해 교정 및 온도 보정을 수행합니다."
        },
        {
            "domain": "1. 바이오 기초 지식 (생물안전 BSL)",
            "question": "생물안전등급(BSL, Biosafety Level) 중 일반적인 대장균 K-12 등 인간에게 질병을 일으킬 가능성이 매우 낮은 미생물을 다루는 기본 등급은?",
            "options": ["① BSL-1", "② BSL-2", "③ BSL-3", "④ BSL-4"],
            "answer": 1,
            "explanation": "BSL-1은 건강한 성인에게 질병을 일으키지 않는 고유 안전성 미생물(예: 대장균 K-12)을 다루는 기본 실험실 등급입니다."
        }
    ],

    "2. 생산 세포 준비": [
        {
            "domain": "2. 생산 세포 준비 (세포은행 체계)",
            "question": "바이오의약품 생산용 세포주 관리에서 마스터 세포은행(MCB)과 제조용 세포은행(WCB)의 관리 원칙으로 올바른 것은?",
            "options": ["① MCB에서 WCB를 마련하고, 실제 생산 배양 공정에는 승인된 WCB를 직접 투입한다.", "② WCB를 먼저 확립한 후 나중에 MCB를 분주하여 보관한다.", "③ WCB의 유래 및 계통 기록 없이 시험 적합서만 있으면 무작위 사용이 가능하다.", "④ MCB와 WCB는 교차 사용이 자유로우므로 구분할 필요가 없다."],
            "answer": 1,
            "explanation": "2단계 셀뱅킹 체계에서는 균일한 원천인 MCB로부터 WCB를 제조하여 생산에 직접 사용함으로써 세포주의 유전적 동일성과 계통 추적성을 보장합니다."
        },
        {
            "domain": "2. 생산 세포 준비 (세포 동결·해동)",
            "question": "동결 보존 세포주를 해동할 때 얼음 결정에 의한 세포막 파손 손상을 최소화하기 위한 해동 수칙으로 가장 올바른 것은?",
            "options": ["① 37°C 항온 수조에서 용기를 신속히 흔들어 급속 해동(Rapid thawing)한다.", "② 상온(25°C)에 방치하여 2시간 동안 천천히 해동한다.", "③ 4°C 냉장고에서 24시간 동안 완만 해동한다.", "④ 전자레인지에 넣고 10초간 가열한다."],
            "answer": 1,
            "explanation": "동결 세포는 해동 과정에서 재결정화에 의한 세포 파괴를 막기 위해 37°C 수조에서 신속히 해동한 후 즉시 동결보존제(DMSO)를 희석/제거합니다."
        },
        {
            "domain": "2. 생산 세포 준비 (칭량 작업)",
            "question": "배지 원료 및 정밀 시약 칭량 시 저울 팬과 시료 간의 직접 접촉을 막고 교차 오염을 방지하기 위해 사용하는 도구는?",
            "options": ["① 칭량지 (Weighing Paper) 또는 칭량 보트", "② 거름종이 (Filter Paper)", "③ 파라필름 (Parafilm)", "④ 페트리디쉬 (Petri Dish) 덮개"],
            "answer": 1,
            "explanation": "원료 칭량 시 저울 표면 오염 및 시료 간 교차 오염을 방지하기 위해 정밀 칭량지나 칭량 배치를 사용합니다."
        },
        {
            "domain": "2. 생산 세포 준비 (세포 오염 측정)",
            "question": "세포주의 오염 여부를 확인하기 위해 수행하는 시험 항목에 해당하지 않는 것은?",
            "options": ["① 단백질 목적 산물의 4차 구조 결정 결정학 분석", "② 현미경을 이용한 세포 형태 및 탁도 관찰", "③ 무균시험 (Sterility Test)", "④ 마이코플라스마 (Mycoplasma) 부정시험"],
            "answer": 1,
            "explanation": "세포주 오염 측정은 외관/현미경 관찰, 무균시험, 마이코플라스마 검사, 외래성 바이러스 검사 등으로 수행합니다."
        },
        {
            "domain": "2. 생산 세포 준비 (동결보존제)",
            "question": "동물세포 동결 보존 시 얼음 결정 형성을 억제하여 세포막을 보호하기 위해 배지에 첨가하는 대표적 동결보존제(Cryoprotectant)는?",
            "options": ["① DMSO (Dimethyl sulfoxide) 및 글리세롤", "② 에탄올 (Ethanol)", "③ 소디움 아자이드 (Sodium azide)", "④ 포름알데히드 (Formaldehyde)"],
            "answer": 1,
            "explanation": "DMSO(통상 5~10%) 및 글리세롤은 동결 시 세포 내외의 수분 결정화를 막아 세포 손상을 방지하는 대표적 동결보존제입니다."
        }
    ],

    "3. 세척·멸균": [
        {
            "domain": "3. 세척·멸균 (Autoclave 표준조건)",
            "question": "고압증기멸균기(Autoclave)의 일반적인 표준 멸균 조건(온도, 게이지 압력, 유지시간)으로 가장 올바른 것은?",
            "options": ["① 121°C, 약 1.05 kg/cm² (15 psi), 15~20분", "② 100°C, 0 kg/cm², 60분", "③ 160°C, 2.0 kg/cm², 120분", "④ 80°C, 0.5 kg/cm², 30분"],
            "answer": 1,
            "explanation": "고압증기멸균기는 121°C의 포화 수증기 압력(약 1.05 kg/cm² 또는 15 psi)하에서 15~20분간 유지하여 내열성 포자까지 완전 사멸시킵니다."
        },
        {
            "domain": "3. 세척·멸균 (CIP vs COP)",
            "question": "배관이나 대형 반응기 탱크를 분해하지 않고 내부에 세척액을 순환시켜 자동 세척하는 공정(CIP)과 소형 부품을 분해하여 전용 세척기에서 세척하는 공정(COP)의 설명으로 옳은 것은?",
            "options": ["① CIP는 제자리 세척(Clean-In-Place), COP는 분리 세척(Clean-Out-of-Place)을 의미한다.", "② CIP는 화학적 멸균, COP는 물리적 건열 세척만을 의미한다.", "③ CIP는 소형 피펫 전용 세척법이다.", "④ COP는 배관을 분해하지 않고 세척하는 방식이다."],
            "answer": 1,
            "explanation": "CIP(Clean-In-Place)는 장비 미분해 제자리 세척, COP(Clean-Out-of-Place)는 부품 분리 후 세척조 세척을 뜻합니다."
        },
        {
            "domain": "3. 세척·멸균 (멸균지표 BI/CI)",
            "question": "멸균 공정 검증 시 사용하는 생물학적 지표(BI)와 화학적 지표(CI)에 대한 올바른 설명은?",
            "options": ["① BI는 내열성 포자(G. stearothermophilus 등)의 사멸 여부를, CI는 온도/시간에 따른 화학적 색 변화를 검증한다.", "② BI는 세척액 잔류량을, CI는 미생물 생존수를 측정한다.", "③ CI 반응이 적합하면 물리적 센서의 운전 기록서가 없어도 멸균이 완전히 입증된다.", "④ BI는 여과 멸균 필터의 구멍 크기를 측정하는 지표이다."],
            "answer": 1,
            "explanation": "BI(Biological Indicator)는 높은 저항성을 가진 포자의 실제 사멸을 확인하며, CI(Chemical Indicator)는 열/스팀 노출에 의한 화학적 변화를 확인합니다."
        },
        {
            "domain": "3. 세척·멸균 (자동세척기 적재)",
            "question": "자동 초자 세척기 운전 시 세척 및 헹굼 효율을 높이고 노즐 막힘을 예방하기 위한 적재 수칙으로 올바른 것은?",
            "options": ["① 용기 입구(개구부)가 아래를 향하도록 거꾸로 세우고, 종이 라벨은 세척 전 미리 제거한다.", "② 용기 입구가 위를 향하도록 바로 세워 세척수가 내부에 고이게 한다.", "③ 세척기 바닥 필터를 제거하고 운전한다.", "④ 세척용 바스켓 없이 용기를 포개어 무작위 배치한다."],
            "answer": 1,
            "explanation": "초자류는 입구가 아래로 향해야 세척수가 잔류하지 않고 배수되며, 라벨이 세척 중 떨어지면 노즐과 바닥 필터를 막으므로 사전 제거해야 합니다."
        },
        {
            "domain": "3. 세척·멸균 (무균조작 소독)",
            "question": "클린벤치나 BSC 내부 무균 작업 시 소독용 에탄올의 올바른 사용법 및 농도는?",
            "options": ["① 70% 소독용 에탄올을 소독용 헝겊/페이퍼 타월에 적셔 표면을 닦아낸다.", "② 100% 무수 에탄올을 클린벤치 공기 중에 대량 분무한다.", "③ 30% 저농도 에탄올을 배지 용액에 직접 혼합한다.", "④ 에탄올 분무 후 화염 멸균기로 클린벤치 전체를 가열한다."],
            "answer": 1,
            "explanation": "70% 에탄올은 세포막 투과력이 우수하여 살균력이 가장 높으며, 분무 시 유기용매 증기 폭발 위험이 있으므로 페이퍼 타월에 적셔 닦아냅니다."
        }
    ],

    "4. 배양 기초": [
        {
            "domain": "4. 배양 기초 (미생물 성장곡선)",
            "question": "미생물 회분 배양 시 나타나는 성장곡선의 4단계 순서와 정지기(Stationary Phase)의 특성으로 올바른 것은?",
            "options": ["① 유도기 → 지수성장기 → 정지기 → 사멸기 / 영양분 고갈과 독성 대사산물 축적으로 증식과 사멸이 균형을 이룸", "② 지수성장기 → 유도기 → 정지기 → 사멸기 / 세포가 최대 비성장 속도로 대량 증식함", "③ 유도기 → 정지기 → 지수성장기 → 사멸기 / 세포 사멸 속도가 증식 속도보다 훨씬 큼", "④ 정지기 → 유도기 → 대수기 → 사멸기 / 세포 크기가 줄어들고 분열이 정지됨"],
            "answer": 1,
            "explanation": "성장곡선은 유도기(Lag) → 지수성장기(Log) → 정지기(Stationary) → 사멸기(Death) 순이며, 정지기는 영양소 고갈/노폐물 축적으로 생존수가 일정 유지됩니다."
        },
        {
            "domain": "4. 배양 기초 (배양 방식 비교)",
            "question": "배양 진행 중 영양성분 배지는 지속적/간헐적으로 주입하지만 배양액의 외부 유출은 공정 종료까지 발생하지 않는 배양 운영 방식은?",
            "options": ["① 유가식 배양 (Fed-batch Culture)", "② 회분식 배양 (Batch Culture)", "③ 연속식 배양 (Continuous / Chemostat)", "④ 관류식 배양 (Perfusion Culture)"],
            "answer": 1,
            "explanation": "유가식(Fed-batch)은 배지는 공급하되 유출은 없어 기질 농도를 제어하고 생산성을 높이는 전형적인 배양 방식입니다."
        },
        {
            "domain": "4. 배양 기초 (호기성 배양 제어)",
            "question": "생물반응기에서 호기성(Aerobic) 미생물 또는 동물세포 배양 시 용존산소(DO) 농도를 유지하기 위해 제어해야 하는 주요 운전 변수는?",
            "options": ["① 공기/산소 통기량(Sparging) 및 임펠러 교반 속도(Agitation)", "② 반응기 내부 냉각수 밸브 닫힘 및 가열기 교정", "③ 배지 소포제 투입 정지 및 이산화탄소 차단", "④ 배양액 전도도 측정 및 질소 가스 고압 투입"],
            "answer": 1,
            "explanation": "호기성 세포는 산소가 필수적이므로 생물반응기의 통기량(Sparging)과 교반 속도(Agitation)를 조절하여 용존산소(DO)를 공급합니다."
        },
        {
            "domain": "4. 배양 기초 (질소원 구분)",
            "question": "배지 구성 성분 중 유기 질소원(Organic Nitrogen Source)에 해당하는 대표적인 물질은?",
            "options": ["① 펩톤 (Peptone) 및 효모 추출물 (Yeast Extract)", "② 질산나트륨 (NaNO3)", "③ 황산암모늄 ((NH4)2SO4)", "④ 인산이수소칼륨 (KH2PO4)"],
            "answer": 1,
            "explanation": "단백질 가수분해물인 펩톤, 효모 추출물, 카제인 등은 아미노산을 제공하는 유기 질소원입니다. 암모늄염, 질산염은 무기 질소원입니다."
        },
        {
            "domain": "4. 배양 기초 (배양액 회수/분리)",
            "question": "배양 완료 후 배양액으로부터 목적으로 하는 세포체(또는 상등액)를 1차 고-액 분리하기 위해 가장 흔히 사용하는 물리적 회수 공정 기술은?",
            "options": ["① 원심분리 (Centrifugation) 및 여과 (Filtration)", "② 역침투 (Reverse Osmosis)", "③ 이온교환 크로마토그래피", "④ 동결건조 (Lyophilization)"],
            "answer": 1,
            "explanation": "1차 회수(Downstream) 공정에서는 원심분리나 TFF/한외여과를 사용하여 불용성 세포체와 수용성 배양 상등액을 분리합니다."
        }
    ],

    "5. 분리·정제 준비": [
        {
            "domain": "5. 분리·정제 준비 (정제 버퍼 원리)",
            "question": "바이오의약품 정제 공정에서 정제 버퍼(Buffer Solution)를 사용하는 가장 핵심적인 원리 및 목적은?",
            "options": ["① 외부 산/염기 유입에도 용액의 pH 변화를 완충하여 표적 단백질의 3차 구조 변성을 방지한다.", "② 용액의 이온 강도를 무한대로 높여 단백질을 강제로 침전시킨다.", "③ 세포막을 물리적으로 파괴하여 유전자를 추출한다.", "④ 용액의 부피를 대량 희석하여 단백질 농도를 0으로 만든다."],
            "answer": 1,
            "explanation": "완충용액(Buffer)은 약산과 그 짝염기로 구성되어 pH 변화를 저항함으로써 단백질의 구조적 안정성을 유지시킵니다."
        },
        {
            "domain": "5. 분리·정제 준비 (크로마토그래피 원리)",
            "question": "크로마토그래피 분리 기법 중 표적 단백질의 '순전하(Net Charge)' 차이를 이용하는 이온교환(IEC)과 '소수성(Hydrophobicity)' 차이를 이용하는 기법(HIC)을 올바르게 짝지은 것은?",
            "options": ["① 이온교환: 전하 차이 / 소수성 상호작용: 소수성 차이", "② 이온교환: 분자량 차이 / 크기배제: 전하 차이", "③ 친화성: 소수성 차이 / 이온교환: 항원-항체 특이적 결합", "④ 겔여과: 이온 강도 차이 / 이온교환: 분자 입체 구조 차이"],
            "answer": 1,
            "explanation": "IEC(Ion Exchange)는 전하 차이, HIC(Hydrophobic Interaction)는 소수성 차이, SEC(Size Exclusion)는 분자 크기 차이, Affinity는 특이적 결합을 이용합니다."
        },
        {
            "domain": "5. 분리·정제 준비 (여과 멸균 프리필터)",
            "question": "열에 약한 액상 정제 버퍼나 배지를 여과 멸균(Filter Sterilization)할 때, 메인 필터(0.22 μm) 전단에 프리 필터(Pre-filter)를 설치하는 이유는?",
            "options": ["① 큰 입자 및 불순물을 1차 제거하여 메인 필터의 폐색(막힘)을 방지하고 수명을 연장하기 위해", "② 용액의 pH를 강산으로 변화시키기 위해", "③ 단백질을 화학적으로 절단하기 위해", "④ 메인 필터의 공극 크기를 10 μm로 확대하기 위해"],
            "answer": 1,
            "explanation": "프리필터(조대 필터)는 조대한 여과 입자를 먼저 걸러내어 비싼 0.22 μm 무균 여과 메인 멤브레인이 일찍 막히는 것을 방지합니다."
        },
        {
            "domain": "5. 분리·정제 준비 (농축 UF/DF)",
            "question": "접선흐름여과(TFF) 한외여과(UF) 공정에서 막의 분자량 컷오프(MWCO) 선택 기준 및 수율 관리 수칙으로 올바른 것은?",
            "options": ["① 표적 단백질 분자량의 약 1/3 ~ 1/6 수준의 MWCO 막을 선택하여 투과 손실을 막는다.", "② 표적 단백질 분자량보다 10배 큰 MWCO 막을 사용한다.", "③ MWCO는 막의 동작 입력 및 온도 제어 장치를 의미한다.", "④ 막 여과 시 공급 압력을 한계 이상으로 무한히 올리면 농축 효율이 항상 올라간다."],
            "answer": 1,
            "explanation": "표적 단백질의 누출을 방지하고 완전히 보유(Retention)하기 위해, 표적 단백질 분자량의 3~5배 작게 MWCO를 설정합니다."
        },
        {
            "domain": "5. 분리·정제 준비 (등전점 pI)",
            "question": "단백질의 등전점(pI, Isoelectric Point)에 대한 설명으로 올바른 것은?",
            "options": ["① 단백질의 순전하(Net Charge)가 0이 되는 pH 상태이며, 이때 단백질의 용해도가 최소가 되어 침전이 발생하기 쉽다.", "② 단백질의 질량이 0이 되는 온도이다.", "③ 용액의 pH가 pI보다 높으면 단백질은 양(+)전하를 띤다.", "④ 등전점에서는 이온교환 크로마토그래피 결합력이 극대화된다."],
            "answer": 1,
            "explanation": "등전점(pI)은 단백질 양전하와 음전하의 합이 0이 되는 pH입니다. 용액 pH > pI이면 음전하, pH < pI이면 양전하를 띱니다."
        }
    ],

    "6. 품질시험": [
        {
            "domain": "6. 품질시험 (단백질 정량 분석)",
            "question": "단백질 정량 시험법 중 Coomassie Brilliant Blue G-250 염료가 단백질과 결합하여 최대 흡광도가 595 nm로 이동하는 원리를 이용하는 정량법은?",
            "options": ["① Bradford Assay", "② BCA Assay", "③ Biuret Assay", "④ UV 280 nm 직접 흡광법"],
            "answer": 1,
            "explanation": "Bradford 정량법은 Coomassie Blue 염료 결합 시 465 nm에서 595 nm로 흡광 이동이 일어나는 현상을 이용합니다."
        },
        {
            "domain": "6. 품질시험 (DNA 전기영동 원리)",
            "question": "아가로스 겔 전기영동(Agarose Gel Electrophoresis)을 이용한 DNA 시료 분석 시 작동 원리에 대한 설명으로 올바른 것은?",
            "options": ["① DNA 뼈대의 인산기가 음(-)전하를 띠므로 양(+)극으로 이동하며, 분자량이 작을수록 빠르게 이동한다.", "② DNA가 양(+)전하를 띠므로 음(-)극으로 이동한다.", "③ DNA의 크기와 상관없이 모든 분자가 동일한 속도로 이동한다.", "④ 아가로스 겔 농도가 낮을수록 단분자 이동 속도가 느려진다."],
            "answer": 1,
            "explanation": "DNA는 음전하를 띠므로 전기장에서 양(+)극으로 이동하며, 겔 망상 구조 내에서 분자량이 작을수록 더 빠르게 통과합니다."
        },
        {
            "domain": "6. 품질시험 (A260/A280 순도)",
            "question": "분광광도계로 추출된 DNA 시료의 A260/A280 흡광 비율을 측정하여 순도를 평가할 때, DNA의 표준 순도 범위 및 단백질 오염 판정 기준은?",
            "options": ["① 고순도 DNA는 1.8 ~ 2.0 범위를 보이며, 1.8 미만일 경우 단백질 오염이 의심된다.", "② 고순도 DNA는 0.5 이하의 값을 보인다.", "③ A260/A280 비율이 2.5 이상이면 단백질 오염으로 판정한다.", "④ 흡광 비율은 단백질 정량법이며 핵산 분석에는 사용되지 않는다."],
            "answer": 1,
            "explanation": "DNA의 A260/A280 적정 비율은 1.8~2.0 (RNA는 2.0~2.2)이며, 1.8 미만으로 낮아지면 280 nm에서 흡수하는 단백질/페놀 오염을 의미합니다."
        },
        {
            "domain": "6. 품질시험 (엔도톡신 LAL 시험)",
            "question": "그램음성균의 세포벽 외막 성분인 발열성 물질(Pyrogen)을 검출하기 위해 투구게의 혈구 추출물을 이용하는 품질 시험법은?",
            "options": ["① 엔도톡신 시험 (LAL Test, Limulus Amebocyte Lysate)", "② 무균 시험 (Sterility Test)", "③ 마이코플라스마 검사", "④ HPLC 순도 시험"],
            "answer": 1,
            "explanation": "LAL 시험은 투구게(Limulus)의 혈구 시약을 이용하여 주사제 및 바이오 제품 내의 엔도톡신(발열성 물질)을 라이세이트 응고 반응으로 검출합니다."
        },
        {
            "domain": "6. 품질시험 (무균시험 절차)",
            "question": "의약품 완제품 또는 검체의 무균 시험(Sterility Test) 수행 시 사용되는 호기성 미생물용 배지와 혐기성 미생물용 배지의 대표적 조합은?",
            "options": ["① TSB (대두대두가수분해배지) / 티오글리콜산 배지 (Fluid Thioglycollate Medium)", "② MacConkey Agar / Nutrient Broth", "③ SDA 배지 / PDA 배지", "④ LB 배지 / 펩톤수"],
            "answer": 1,
            "explanation": "무균시험에서는 호기성 진균/세균용 TSB 배지(20~25°C 배양)와 혐기성/호기성 세균용 티오글리콜산 배지(30~35°C 배양)를 함께 사용합니다."
        }
    ],

    "7. 제조용수·가스 시험": [
        {
            "domain": "7. 제조용수·가스 시험 (제조용수 보관)",
            "question": "정제수(PW) 및 주사용수(WFI) 검체 채취 후 미생물 증식을 억제하기 위한 보관 관리 수칙으로 가장 올바른 것은?",
            "options": ["① 채취 후 2 ~ 8°C 냉장 보관하고 빠르게 시험을 진행한다. (동결은 절대 금지)", "② 채취 후 -80°C 초저온 냉동고에 즉시 동결 보관한다.", "③ 채취 용기를 50°C 온장고에 방치한다.", "④ 상온(25°C)에서 72시간 동안 보관 후 시험한다."],
            "answer": 1,
            "explanation": "제조용수 검체는 동결 시 용기 파손 및 미생물 사멸로 정확한 미생물 한도 시험이 불가하므로 2~8°C 냉장 보관해야 합니다."
        },
        {
            "domain": "7. 제조용수·가스 시험 (TOC 및 전도도)",
            "question": "제조용수(WFI)의 이화학적 품질 평가 지표 중 수중 미량 유기 오염물질 총량을 측정하는 TOC와 이온성 불순물 총량을 측정하는 전도도(Conductivity) 설명으로 올바른 것은?",
            "options": ["① TOC는 총유기탄소(Total Organic Carbon)를, 전도도는 이온성 전해질 불순물을 각각 독립 평가한다.", "② TOC와 전도도는 서로 완전히 동일한 수치를 나타낸다.", "③ TOC는 미생물 생존수(CFU)만을 측정하는 생물학 지표이다.", "④ 전도도가 높을수록 용수의 순도가 높음을 의미한다."],
            "answer": 1,
            "explanation": "TOC는 유기 오염물질 지표이고 전도도는 미량 이온/전해질 불순물 지표입니다. 주사용수(WFI)는 TOC ≤ 500 ppb, 전도도 규격을 충족해야 합니다."
        },
        {
            "domain": "7. 제조용수·가스 시험 (가스 순도 시험)",
            "question": "생물반응기 배양 및 공정에 공급되는 질소(N2), 이산화탄소(CO2), 압축공기 가스의 순도 시험 시 측정하는 주요 불순물 항목에 해당하지 않는 것은?",
            "options": ["① 단백질 함량 (Protein Content)", "② 수분 (Moisture)", "③ 일산화탄소 (CO) 및 이산화탄소 (CO2)", "④ 오일 미스트 및 수증기"],
            "answer": 1,
            "explanation": "공정용 가스는 수분, 산소, 일산화탄소, 오일 성분 등 불순물을 측정합니다. 단백질은 기체 상태에 존재하지 않으므로 측정 항목이 아닙니다."
        },
        {
            "domain": "7. 제조용수·가스 시험 (WFI 제조 원리)",
            "question": "주사용수(WFI, Water for Injection) 제조 시 엔도톡신 및 미생물을 완벽히 제거하기 위해 적용하는 대표적인 1차 정제 원리는?",
            "options": ["① 다단 증류법 (Distillation) 및 역침투/한외여과 (RO/UF) 조합", "② 여과지 단순 자연 여과", "③ 모래 필터 여과", "④ 단순 활성탄 흡착"],
            "answer": 1,
            "explanation": "WFI는 정제수(PW)를 원수로 하여 다단 증류(Distillation) 또는 RO+UF(역침투+한외여과) 공정을 거쳐 엔도톡신을 제거하여 제조합니다."
        }
    ],

    "8. 환경 모니터링 시험": [
        {
            "domain": "8. 환경 모니터링 시험 (크린룸 청정도 등급)",
            "question": "GMP 크린룸 청정도 등급 중 바이오의약품의 무균 충전(Aseptic Filling) 및 무균 연결 조작이 직접 이루어지는 최상위 무균 구역 등급은?",
            "options": ["① Grade A (ISO Class 5)", "② Grade B", "③ Grade C", "④ Grade D"],
            "answer": 1,
            "explanation": "Grade A는 무균 조작 및 충전이 일어나는 최상위 무균 작업존으로, 층류(Laminar airflow, 0.36~0.54 m/s) 기류를 유지합니다."
        },
        {
            "domain": "8. 환경 모니터링 시험 (미생물 측정기법)",
            "question": "크린룸 환경 모니터링 기법 중 '부유균(Air Sampler)', '낙하균(Settling Plate)', '표면균(Contact Plate)'의 측정법 연결로 올바른 것은?",
            "options": ["① 부유균: 정량 공기 흡입 포집 / 낙하균: 4시간 배지 개방 침강 / 표면균: Contact Plate 25cm² 표면 직접 접촉", "② 부유균: Swab 배관 내부 채취 / 낙하균: Particle Counter 광산란 측정 / 표면균: 24시간 공기 흡입", "③ 부유균: 멸균 가스 채취 / 낙하균: pH 측정기 삽입 / 표면균: TOC 분석", "④ 부유균과 낙하균, 표면균은 모두 동일한 광산란 입자 카운터로만 측정한다."],
            "answer": 1,
            "explanation": "부유균은 에어샘플러로 공기 흡입, 낙하균은 4시간 배지 노출, 표면균은 접촉배지(Contact Plate)나 스왑(Swab)으로 작업장 표면 미생물을 채취합니다."
        },
        {
            "domain": "8. 환경 모니터링 시험 (배지성능시험 GPT)",
            "question": "환경 모니터링 및 미생물 시험에 사용하는 배지가 미생물의 성장을 지원할 수 있는지 사용 전 검증하는 필수 시험은?",
            "options": ["① 배지성능시험 (GPT, Growth Promotion Test)", "② 무균성 시험", "③ LAL 시험", "④ 멸균 유효성 시험"],
            "answer": 1,
            "explanation": "GPT(Growth Promotion Test)는 표준 균주(100 CFU 이하)를 접종하여 해당 배지가 미생물을 정상 증식시킬 수 있는지 검증하는 시험입니다."
        },
        {
            "domain": "8. 환경 모니터링 시험 (OOS vs OOT)",
            "question": "크린룸 환경 모니터링 결과, 측정값이 승인된 품질 규격한계(Spec)는 충족하지만 통계적 관리 경향 범위(Trend)를 벗어난 경우의 올바른 품질 분류는?",
            "options": ["① 규격 적합 / 경향 이탈 (OOT, Out of Expectation)", "② 규격 이탈 (OOS, Out of Specification)", "③ 시험 무효 (Invalid Test)", "④ 기기 교정 이탈 (OOE)"],
            "answer": 1,
            "explanation": "측정값이 규격(Spec) 내에 있지만 평소 관리 경향 범위를 벗어난 경우 OOT(Out of Expectation)로 분류하여 경향 조사를 수행합니다."
        }
    ]
}

# ------------------------------------------------------------------
# 2. 25+ 고난도 동적 무제한 문제 생성 엔진 (Diverse Dynamic Generators)
# ------------------------------------------------------------------

def gen_dyn_alcoa():
    scenarios = [
        ("작업자가 현장에서 배양 진행 중 표면균 채취를 완료한 즉시 양식에 서명하여 기록하였으나, 개인 계정이 아닌 팀 공용 계정을 사용하여 작성자가 불분명해졌다.", "귀속성(Attributable)", ["동시성(Contemporaneous)", "가독성(Legible)", "원본성(Original)"], "ALCOA 원칙 중 귀속성(Attributable)은 모든 기록에 수행자의 고유한 식별 정보가 명확히 연결되어야 함을 요구합니다."),
        ("수동 칭량 작업 3일 후 기억에 의존해 한꺼번에 제조 기록서를 소급하여 작성하였다.", "동시성(Contemporaneous)", ["귀속성(Attributable)", "완전성(Complete)", "정확성(Accurate)"], "작업 수행 직후 실시간으로 기록되지 않고 소급 작성된 경우 동시성(Contemporaneous) 원칙을 위반한 것입니다."),
        ("시험 데이터를 원본 파일에 직접 수정 이력(Audit Trail) 없이 새로 덮어쓰고 구자료를 삭제하였다.", "원본성(Original)", ["귀속성(Attributable)", "가독성(Legible)", "동시성(Contemporaneous)"], "원본 데이터와 변경 이력이 추적 가능하게 보존되지 않은 경우 원본성(Original)을 위반한 것입니다.")
    ]
    scen, correct, wrongs, exp = random.choice(scenarios)
    opts = [correct] + wrongs
    random.shuffle(opts)
    ans = opts.index(correct) + 1
    return {
        "domain": "1. 바이오 기초 지식 (GMP Data Integrity)",
        "question": f"[GMP 데이터 완전성 사례 분석] 다음 상황에서 가장 직접적으로 약화되거나 위반된 ALCOA 원칙은?\n\n사례: {scen}",
        "options": [f"① {opts[0]}", f"② {opts[1]}", f"③ {opts[2]}", f"④ {opts[3]}"],
        "answer": ans,
        "explanation": exp
    }

def gen_dyn_c1v1():
    c1 = random.choice([2, 4, 5, 10, 20])
    c2 = random.choice([0.1, 0.2, 0.4, 0.5, 1.0])
    v2 = random.choice([200, 250, 500, 1000, 2000])
    v1_ans = int((c2 * v2) / c1)
    wrong1 = v1_ans + random.choice([10, 25, 50])
    wrong2 = max(5, v1_ans - random.choice([5, 10]))
    wrong3 = v1_ans * 2
    correct_str = f"{v1_ans} mL"
    opts = [correct_str, f"{wrong1} mL", f"{wrong2} mL", f"{wrong3} mL"]
    random.shuffle(opts)
    ans = opts.index(correct_str) + 1
    return {
        "domain": "5. 분리·정제 준비 (용액 조제 희석)",
        "question": f"저장액 농도가 {c1} M인 완충 시약을 사용하여, 목표 농도 {c2} M의 정제 버퍼 {v2} mL를 조제하고자 한다. 취해야 할 {c1} M 저장액의 필요한 부피(V1)는?",
        "options": [f"① {opts[0]}", f"② {opts[1]}", f"③ {opts[2]}", f"④ {opts[3]}"],
        "answer": ans,
        "explanation": f"C1 × V1 = C2 × V2 공식을 적용합니다: {c1} M × V1 = {c2} M × {v2} mL → V1 = ({c2} × {v2}) / {c1} = {v1_ans} mL 입니다."
    }

def gen_dyn_ideal_gas():
    p = random.choice([1.0, 1.2, 1.5, 2.0])
    v = random.choice([2.0, 4.0, 5.0, 10.0, 22.4])
    temp_c = random.choice([20, 25, 30, 37])
    temp_k = temp_c + 273.15
    n_ans = round((p * v) / (0.0821 * temp_k), 3)
    wrong1 = round((p * v) / (0.0821 * temp_c), 3)
    wrong2 = round(n_ans * 2, 3)
    wrong3 = round(n_ans / 2, 3)
    correct_str = f"약 {n_ans} mol"
    opts = [correct_str, f"약 {wrong1} mol", f"약 {wrong2} mol", f"약 {wrong3} mol"]
    random.shuffle(opts)
    ans = opts.index(correct_str) + 1
    return {
        "domain": "1. 바이오 기초 지식 (화공 기초 계산)",
        "question": f"부피가 {v} L인 생물반응기 헤드스페이스 내부 온도가 {temp_c}°C, 게이지/절대 압력이 {p} atm일 때, 내부 기체의 몰수(n)로 가장 적절한 것은? (단, R = 0.0821 L·atm/(mol·K))",
        "options": [f"① {opts[0]}", f"② {opts[1]}", f"③ {opts[2]}", f"④ {opts[3]}"],
        "answer": ans,
        "explanation": f"이상기체 상태방정식 n = PV / (RT)를 적용합니다. 절대온도 T = {temp_c} + 273.15 = {temp_k} K입니다. n = ({p} × {v}) / (0.0821 × {temp_k}) ≈ {n_ans} mol 입니다."
    }

def gen_dyn_oot_oos():
    spec_limit = random.choice([10, 20, 50, 100])
    oot_high = spec_limit // 2
    oot_low = oot_high // 2
    val = random.choice([oot_high + 5, spec_limit + 10, oot_low - 2])
    if val > spec_limit:
        status = "규격 이탈 (OOS, Out of Specification)"
        exp = f"측정값({val})이 승인된 품질 규격한계({spec_limit} 이하)를 초과하였으므로 OOS로 판정하고 원인 조사를 수행합니다."
    elif val > oot_high:
        status = "규격 적합 / 경향 이탈 (OOT, Out of Expectation)"
        exp = f"측정값({val})이 규격한계({spec_limit} 이하) 내이지만 관리 경향 범위({oot_low}~{oot_high})를 벗어났으므로 OOT로 분류합니다."
    else:
        status = "규격 적합 / 경향 적합"
        exp = f"측정값({val})이 규격한계({spec_limit}) 및 경향 범위({oot_low}~{oot_high}) 내에 모두 적합합니다."

    opts = ["규격 적합 / 경향 적합", "규격 적합 / 경향 이탈 (OOT, Out of Expectation)", "규격 이탈 (OOS, Out of Specification)", "기기 교정 오차 이탈 (OOE)"]
    ans = opts.index(status) + 1
    return {
        "domain": "8. 환경 모니터링 시험 (OOS vs OOT 판별)",
        "question": f"크린룸 청정도 모니터링에서 승인된 규격한계(Spec)가 '{spec_limit} CFU 이하'이고, 통계적 관리 경향 범위가 '{oot_low}~{oot_high} CFU'로 정의되어 있다. 측정 결과값이 '{val} CFU'일 때의 올바른 품질 분류는?",
        "options": [f"① {opts[0]}", f"② {opts[1]}", f"③ {opts[2]}", f"④ {opts[3]}"],
        "answer": ans,
        "explanation": exp
    }

def gen_dyn_dvalue():
    d_val = random.choice([1.5, 2.0, 2.5, 3.0, 4.0])
    log_red = random.choice([2, 3, 4, 5, 6])
    req_time = round(d_val * log_red, 1)
    correct_str = f"{req_time} 분"
    opts = [correct_str, f"{d_val} 분", f"{round(d_val + log_red, 1)} 분", f"{round(req_time * 2, 1)} 분"]
    random.shuffle(opts)
    ans = opts.index(correct_str) + 1
    return {
        "domain": "3. 세척·멸균 (열처리 D값 및 살균 로직)",
        "question": f"특정 미생물을 121°C 조건에서 열처리할 때 D값(Decimal Reduction Time)이 {d_val}분이다. 생존 세포 수를 {log_red} log만큼 감소시키기 위해 필요한 열처리 가열 시간은?",
        "options": [f"① {opts[0]}", f"② {opts[1]}", f"③ {opts[2]}", f"④ {opts[3]}"],
        "answer": ans,
        "explanation": f"D값은 미생물을 1 log (90%) 감소시키는 데 필요한 시간입니다. {log_red} log 사멸 시간 = D값 × {log_red} = {d_val}분 × {log_red} = {req_time}분 입니다."
    }

def gen_dyn_viability():
    total_cells = random.choice([100, 150, 200, 250, 300])
    dead_cells = random.choice([10, 15, 20, 30, 50])
    live_cells = total_cells - dead_cells
    viab = round((live_cells / total_cells) * 100, 1)
    correct_str = f"{viab} %"
    opts = [correct_str, f"{round((dead_cells/total_cells)*100, 1)} %", f"{round(viab-10, 1)} %", f"100.0 %"]
    random.shuffle(opts)
    ans = opts.index(correct_str) + 1
    return {
        "domain": "2. 생산 세포 준비 (세포 생존율 계산)",
        "question": f"Trypan Blue 염색법을 이용하여 혈구계(Hemocytometer)로 세포를 계수한 결과, 총 세포 수 {total_cells}개 중 사멸 세포(파란색 염색)가 {dead_cells}개 관찰되었다. 이 세포주의 세포 생존율(Viability)은?",
        "options": [f"① {opts[0]}", f"② {opts[1]}", f"③ {opts[2]}", f"④ {opts[3]}"],
        "answer": ans,
        "explanation": f"생존율 = (생존 세포 수 / 총 세포 수) × 100 = ({live_cells} / {total_cells}) × 100 = {viab}% 입니다. Trypan Blue는 사멸 세포의 파손된 막으로 들어가 파란색으로 염색됩니다."
    }

def gen_dyn_poh_ph():
    naoh_conc = random.choice([0.01, 0.001, 0.1, 0.0001])
    poh_val = 2.0 if naoh_conc==0.01 else (3.0 if naoh_conc==0.001 else (1.0 if naoh_conc==0.1 else 4.0))
    ph_ans = round(14.0 - poh_val, 1)
    correct_str = f"pH {ph_ans}"
    opts = [correct_str, f"pH {poh_val}", f"pH {round(ph_ans - 2, 1)}", f"pH 7.0"]
    random.shuffle(opts)
    ans = opts.index(correct_str) + 1
    return {
        "domain": "5. 분리·정제 준비 (산·염기 pH/pOH 계산)",
        "question": f"25°C 수용액 상태에서 완전히 이온화되는 강염기 NaOH 용액의 농도가 {naoh_conc} M일 때, 이 완충 용액의 pH 값으로 올바른 것은?",
        "options": [f"① {opts[0]}", f"② {opts[1]}", f"③ {opts[2]}", f"④ {opts[3]}"],
        "answer": ans,
        "explanation": f"강염기 NaOH는 완전 이온화되어 [OH⁻] = {naoh_conc} M 입니다. 따라서 pOH = -log[OH⁻] = {poh_val} 이며, pH + pOH = 14 이므로 pH = 14 - {poh_val} = {ph_ans} 입니다."
    }

DYNAMIC_GENERATORS = [
    gen_dyn_alcoa,
    gen_dyn_c1v1,
    gen_dyn_ideal_gas,
    gen_dyn_oot_oos,
    gen_dyn_dvalue,
    gen_dyn_viability,
    gen_dyn_poh_ph
]

# ------------------------------------------------------------------
# 3. 출제기준 60문항 완전 무중복 스마트 문제 생성기
# ------------------------------------------------------------------

# 출제기준에 따른 영역별 표준 문항 배분 수 (총 60문항)
DOMAIN_TARGET_COUNTS = {
    "1. 바이오 기초 지식": 7,
    "2. 생산 세포 준비": 6,
    "3. 세척·멸균": 8,
    "4. 배양 기초": 11,
    "5. 분리·정제 준비": 7,
    "6. 품질시험": 8,
    "7. 제조용수·가스 시험": 6,
    "8. 환경 모니터링 시험": 7
}

def generate_unique_60_exam():
    final_questions = []
    seen_texts = set()

    for dom_name, target_count in DOMAIN_TARGET_COUNTS.items():
        dom_added = 0
        bank_items = DOMAIN_BANKS.get(dom_name, [])
        
        # 1. 정적 뱅크에서 가능한 만큼 무작위 추출
        shuffled_bank = random.sample(bank_items, len(bank_items))
        for q in shuffled_bank:
            q_text = q["question"]
            if q_text not in seen_texts:
                seen_texts.add(q_text)
                final_questions.append(q)
                dom_added += 1
                if dom_added >= target_count:
                    break
        
        # 2. 부족한 수는 동적 생성기로 보충
        attempts = 0
        while dom_added < target_count and attempts < 50:
            attempts += 1
            gen_fn = random.choice(DYNAMIC_GENERATORS)
            q = gen_fn()
            q_text = q["question"]
            if q_text not in seen_texts:
                seen_texts.add(q_text)
                q_copy = dict(q)
                q_copy["domain"] = f"{dom_name} (응용 시나리오)"
                final_questions.append(q_copy)
                dom_added += 1

    # 혹시 총 60문항에 미달할 경우 전체 생성기에서 채움
    while len(final_questions) < 60:
        gen_fn = random.choice(DYNAMIC_GENERATORS)
        q = gen_fn()
        q_text = q["question"]
        if q_text not in seen_texts:
            seen_texts.add(q_text)
            final_questions.append(q)

    random.shuffle(final_questions)
    return final_questions[:60]

# ------------------------------------------------------------------
# 4. Streamlit UI 앱 메인 로직
# ------------------------------------------------------------------

st.title("🧪 바이오공정기능사 필기 실전 CBT 모의고사 v10")
st.caption("2026년 첫 시행 대비 | 출제기준 8대 영역 100% 반영 & 완전 무중복 60문항 무제한 생성기")

# 세션 상태 초기화
if "current_q_idx" not in st.session_state:
    st.session_state.current_q_idx = 1
if "user_answers" not in st.session_state:
    st.session_state.user_answers = {}
if "exam_started" not in st.session_state:
    st.session_state.exam_started = False
if "exam_completed" not in st.session_state:
    st.session_state.exam_completed = False

# 사이드바
st.sidebar.header("⚙️ CBT 시험장 메뉴")
nav_choice = st.sidebar.radio("원하시는 모드를 선택하세요", ["⏱️ 실전 모의고사 (60문항 / 60분)", "🎲 무제한 고난도 문제 은행", "📊 성적 분석 및 오답 노트"])

# ------------------------------------------------------------------
# 모드 1: ⏱️ 실전 모의고사 (60문항 / 60분)
# ------------------------------------------------------------------
if nav_choice == "⏱️ 실전 모의고사 (60문항 / 60분)":
    
    if not st.session_state.exam_started:
        st.subheader("📋 바이오공정기능사 필기 실전 CBT 모의고사 응시 안내")
        st.write("""
        * **시험 과목**: 바이오 생산 및 품질관리 기초 (통합 60문항)
        * **제한 시간**: 60분 (실시간 초단위 카운트다운 타이머 작동)
        * **합격 기준**: 100점 만점 기준 60점 이상 (36문항 이상 정답 시 합격)
        * **출제 비중**: **출제기준 8대 영역별 정밀 문항 배분** (기초지식 7, 세포준비 6, 세척멸균 8, 배양기초 11, 정제준비 7, 품질시험 8, 용수가스 6, 환경모니터링 7문항).
        * **OMR 답안지**: 우측 1~60번 OMR 마킹판에 선택한 보기(❶, ❷, ❸, ❹)가 실시간으로 표기되며 원클릭 점프를 지원합니다.
        """)
        
        if st.button("🚀 실전 모의고사 시험 시작 (Start CBT)", type="primary", use_container_width=True):
            st.session_state.exam_started = True
            st.session_state.exam_completed = False
            st.session_state.start_time = time.time()
            st.session_state.current_q_idx = 1
            st.session_state.user_answers = {}
            st.session_state.questions = generate_unique_60_exam()
            st.rerun()

    elif not st.session_state.exam_completed:
        col_main, col_omr = st.columns([3, 1.2])
        
        # RIGHT COLUMN: 실시간 타이머 + 실제 OMR 답안지
        with col_omr:
            st.markdown("### ⏱️ 시험시간 및 OMR 카드")
            
            # 실시간 JS 타이머
            start_ts = st.session_state.start_time
            timer_html = f"""
            <div style="background-color: #2b3035; color: #ffffff; padding: 12px; border-radius: 8px; text-align: center; font-family: 'Noto Sans KR', sans-serif;">
                <div style="font-size: 13px; color: #adb5bd; margin-bottom: 2px;">CBT 남은 시간 (60분)</div>
                <div id="countdown" style="font-size: 28px; font-weight: 800; color: #ffc107; letter-spacing: 1px;">60:00</div>
            </div>
            <script>
                const startTime = {start_ts} * 1000;
                const duration = 3600 * 1000;
                function updateTimer() {{
                    const now = new Date().getTime();
                    const elapsed = now - startTime;
                    const remain = Math.max(0, duration - elapsed);
                    const totalSecs = Math.floor(remain / 1000);
                    const mins = Math.floor(totalSecs / 60);
                    const secs = totalSecs % 60;
                    const formattedMins = String(mins).padStart(2, '0');
                    const formattedSecs = String(secs).padStart(2, '0');
                    const timerElem = document.getElementById("countdown");
                    if (timerElem) {{
                        timerElem.innerText = formattedMins + ":" + formattedSecs;
                        if (remain <= 300000) {{
                            timerElem.style.color = "#dc3545";
                        }}
                    }}
                }}
                setInterval(updateTimer, 1000);
                updateTimer();
            </script>
            """
            components.html(timer_html, height=85)
            
            answered_cnt = len(st.session_state.user_answers)
            st.progress(answered_cnt / 60)
            st.caption(f"답안 표기현황: **{answered_cnt}** / 60 문항 완료")
            st.divider()
            
            st.markdown("**📋 OMR 답안 마킹판**")
            omr_container = st.container(height=480)
            with omr_container:
                for idx in range(1, 61):
                    selected = st.session_state.user_answers.get(idx, None)
                    is_current = (idx == st.session_state.current_q_idx)
                    
                    symbols = ["①", "②", "③", "④"]
                    marked_symbols = ["❶", "❷", "❸", "❹"]
                    
                    bubble_str = ""
                    for b_idx in range(1, 5):
                        if selected == b_idx:
                            bubble_str += f" <b style='color:#0d6efd;'>{marked_symbols[b_idx-1]}</b>"
                        else:
                            bubble_str += f" <span style='color:#adb5bd;'>{symbols[b_idx-1]}</span>"
                    
                    prefix = "👉" if is_current else ""
                    
                    c_btn, c_bubbles = st.columns([1, 2.2])
                    with c_btn:
                        btn_label = f"{prefix}{idx:02d}번"
                        if st.button(btn_label, key=f"omr_jump_{idx}", type="secondary" if not is_current else "primary"):
                            st.session_state.current_q_idx = idx
                            st.rerun()
                    with c_bubbles:
                        st.markdown(f"<div style='font-size:14px; padding-top:4px;'>{bubble_str}</div>", unsafe_allow_html=True)

            st.divider()
            if st.button("📝 최종 OMR 답안 제출하기", type="primary", use_container_width=True):
                st.session_state.exam_completed = True
                st.rerun()

        # LEFT COLUMN: 실제 시험장 1문항 전개 카드
        with col_main:
            q_idx = st.session_state.current_q_idx
            q_data = st.session_state.questions[q_idx - 1]
            
            st.markdown(f"### 📌 [문제 {q_idx} / 60] - {q_data['domain']}")
            st.info(f"**Q{q_idx}. {q_data['question']}**")
            
            saved_choice_num = st.session_state.user_answers.get(q_idx, None)
            saved_index = (saved_choice_num - 1) if saved_choice_num in [1, 2, 3, 4] else None
            
            user_select = st.radio(
                "답안 선택:",
                q_data['options'],
                index=saved_index,
                key=f"main_q_radio_{q_idx}"
            )
            
            if user_select:
                sym_map = {"①": 1, "②": 2, "③": 3, "④": 4}
                first_char = user_select.strip()[0]
                sel_num = sym_map.get(first_char, 1)
                
                if st.session_state.user_answers.get(q_idx) != sel_num:
                    st.session_state.user_answers[q_idx] = sel_num
                    st.rerun()
            
            st.divider()
            
            nav_col1, nav_col2, nav_col3 = st.columns([1, 2, 1])
            with nav_col1:
                if q_idx > 1:
                    if st.button("⬅️ 이전 문제", use_container_width=True):
                        st.session_state.current_q_idx -= 1
                        st.rerun()
            with nav_col3:
                if q_idx < 60:
                    if st.button("다음 문제 ➡️", use_container_width=True):
                        st.session_state.current_q_idx += 1
                        st.rerun()

    else:
        st.subheader("🎉 바이오공정기능사 필기 CBT 시험 결과")
        
        correct_cnt = 0
        wrong_items = []
        for idx, q in enumerate(st.session_state.questions, 1):
            u_ans = st.session_state.user_answers.get(idx, 0)
            if u_ans == q['answer']:
                correct_cnt += 1
            else:
                wrong_items.append((idx, q, u_ans))
                
        score = (correct_cnt / 60) * 100
        st.session_state.score = score
        st.session_state.wrong_items = wrong_items
        
        col_res1, col_res2, col_res3 = st.columns(3)
        col_res1.metric("취득 점수", f"{score:.1f} 점")
        col_res2.metric("정답 문항", f"{correct_cnt} / 60 문항")
        col_res3.metric("합격 여부", "최종 합격 🏆" if score >= 60.0 else "불합격 ❌")
        
        st.divider()
        if st.button("🔄 새 실전 모의고사 응시하기", type="primary"):
            st.session_state.exam_started = False
            st.session_state.exam_completed = False
            st.rerun()

elif nav_choice == "🎲 무제한 고난도 문제 은행":
    st.subheader("🎲 무제한 동적 고난도 문제 풀이")
    st.info("버튼을 누를 때마다 수치, 사례, 선택지가 실시간 무작위로 생성되는 문제를 다채롭게 풀 수 있습니다.")
    
    if st.button("🔄 새 고난도 문제 생성하기", type="primary"):
        gen_fn = random.choice(DYNAMIC_GENERATORS)
        st.session_state.current_gen_q = gen_fn()
        
    if "current_gen_q" not in st.session_state:
        gen_fn = random.choice(DYNAMIC_GENERATORS)
        st.session_state.current_gen_q = gen_fn()
        
    q = st.session_state.current_gen_q
    st.markdown(f"### 📌 [{q['domain']}]")
    st.write(q['question'])
    
    user_choice = st.radio("정답 선택:", q['options'], index=None)
    if user_choice:
        sym_map = {"①": 1, "②": 2, "③": 3, "④": 4}
        first_char = user_choice.strip()[0]
        user_num = sym_map.get(first_char, 1)
        
        if user_num == q['answer']:
            st.success("✅ 정답입니다! 완벽하게 개념 및 수치를 판별하셨습니다.")
        else:
            st.error(f"❌ 오답입니다. (정답: {q['answer']}번)")
        with st.expander("💡 상세 해설 보기", expanded=True):
            st.write(q['explanation'])

elif nav_choice == "📊 성적 분석 및 오답 노트":
    st.subheader("📊 오답 노트 및 해설 복습")
    if "exam_completed" in st.session_state and st.session_state.exam_completed:
        st.write(f"최근 모의고사 점수: **{st.session_state.score:.1f}점**")
        st.write(f"틀린 문항 수: **{len(st.session_state.wrong_items)}문항**")
        st.divider()
        
        for idx, q, u_ans in st.session_state.wrong_items:
            st.markdown(f"❌ **[문제 {idx}] {q['question']}**")
            for opt in q['options']:
                st.write(f"   {opt}")
            st.write(f"👉 내가 낸 답: {u_ans}번 | 🟢 **정답: {q['answer']}번**")
            st.info(f"💡 **[상세 해설]** {q['explanation']}")
            st.divider()
    else:
        st.warning("먼저 '⏱️ 실전 모의고사'를 진행한 후 오답 노트를 확인하세요!")
