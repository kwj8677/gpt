# 디지털 시네마는 15/70 IMAX를 물리적·지각적으로 대체할 수 있는가?

## 공간주파수, 광화학 전달함수, 인간 시각, 대형 CMOS 및 직시형 시네마를 통한 제일원칙 분석

**English title:** *Can Digital Cinema Physically and Perceptually Supersede 15/70 IMAX? — A First-Principles Analysis of Spatial Information, Photochemical Transfer Functions, Human Vision, Large-Format CMOS, and Direct-View Cinema*

**저자:** Yeon-Jin Kim · Independent Research  
**문서 성격:** 독립 기술 연구 논문 / doctoral-style technical research manuscript  
**버전:** 1.0  
**기준일:** 2026-08-17  
**언어:** 한국어, 영문 초록 병기

> **주의:** 본 문서는 학위 수여를 위한 박사학위논문이나 동료평가(peer review)를 거친 학술지 논문이 아니다. 박사학위 논문 수준의 문제정의·정량화·반증 가능성·실험설계를 지향한 독립 기술 연구 원고다.

---

## 초록

15/70 IMAX 필름은 수십 년 동안 극장용 영상 포맷의 최상위 기준으로 간주되어 왔다. 그러나 그 우위의 원인을 단순히 1.43:1 화면비, ‘18K급’이라는 관용적 해상도 표현, 또는 필름이라는 아날로그 매체의 신비성으로 설명하는 것은 물리적으로 불충분하다. 본 연구는 IMAX의 역사적 우위를 **장면(scene) → 렌즈 → 감광 유제 또는 이미지 센서 → 신호 처리 → 마스터 → 투사/직시 디스플레이 → 인간 시각계**라는 종단 간(end-to-end) 정보전달 시스템으로 재구성한다. 핵심 질문은 ‘필름과 디지털 중 어느 쪽이 더 감성적인가’가 아니라, **현대 디지털 시스템이 15/70 필름 체인에서 인간에게 지각 가능한 정보를 모두 측정·보존·재현할 수 있는가**이다.

필름은 수학적 의미의 무한해상도 연속체가 아니다. 실제 네거티브는 렌즈의 점확산함수(PSF), 필름 유제의 MTF, 광자 통계, 입자성(granularity), 유제 내 산란, 현상 화학, 색감광층의 분광감도에 의해 유한한 신호대잡음비와 공간주파수 응답을 갖는다. 따라서 ‘15/70 IMAX = 정확히 18K’와 같은 등식은 엄밀한 물리량이 아니다. 해상도는 장면 대비, 노출, 렌즈, 필름 스톡, 현상, MTF 임계치와 허용 가능한 신호대잡음비에 따라 달라진다. 본 연구는 이를 고정된 K 숫자가 아니라 **MTF와 지각 임계치의 함수**로 다룬다.

2026년 현재 상용 디지털 기술은 이미 이 논쟁의 전제를 크게 바꾸었다. Blackmagic URSA Cine 17K 65는 50.81 × 23.32 mm 센서에서 17,520 × 8,040, 2.9 μm 픽셀피치, 16-stop 동적범위, 최대 17K 60 fps를 제공한다. Canon은 35 mm 풀프레임 면적에 24,592 × 16,704, 410 MP의 CMOS를 시연했다. Lasergraphics Director는 IMAX/65/70 mm 필름을 최대 13.5K, 순차 RGB 방식으로 스캔한다. 삼성 Onyx Cinema LED는 2026년형에서 최대 20 m 확장, 4K/120 Hz, 최대 300 nit의 직시형 시네마를 상용화했다. 이 기술들은 **한 제품에 동시에 결합되어 있지는 않지만**, 대형면적·고픽셀밀도·고속 readout·고해상도 필름 디지타이징·대형 직시형 상영이라는 각각의 물리적 서브문제가 이미 해결 가능한 범위에 들어왔음을 보여준다.

인간 시각 측면에서도 고정된 ‘60 pixels/degree = retina’ 가정은 충분하지 않다. 2025년 *Nature Communications* 연구는 중심와(foveal) 무채색 패턴에서 약 94 pixels/degree(ppd)에 이르는 분해능을 보고했으며, 개인차와 자극 조건에 따라 더 높은 한계가 존재한다. 이를 매우 넓은 100° 수평 시야각의 극장에 적용하면 약 9.4K가 94 ppd에 해당하며, 120 ppd를 보수적 상한으로 두면 약 12K가 된다. 따라서 **대형 극장에서는 8K를 넘어서는 해상도가 무조건 무의미하다고 말할 수도 없고, 반대로 18K가 필수라고 말할 근거도 없다.** 해상도 요구량은 좌석별 시야각과 인간 시각 특성으로 계산되어야 한다.

본 논문의 결론은 ‘디지털이 이미 15/70 IMAX를 완벽히 대체했다’가 아니다. 더 정확한 결론은 다음과 같다. **15/70 IMAX의 공간정보량 우위는 더 이상 디지털 기술의 근본적 물리 한계가 아니다.** 현재의 주요 병목은 초대형 센서의 수율·readout·열·다이내믹레인지, 12K급 종단 후반작업, 대형 직시 디스플레이의 비용·균일도·전력·음향 통합, 그리고 필름의 비선형·확률적 전달특성을 지각적으로 동등하게 재현하는 모델링이다. 최종 판정은 마케팅 수치가 아니라 **동일 장면에 대한 통제된 2AFC/ABX 이중맹검 지각실험**으로 이루어져야 한다.

**핵심어:** IMAX 15/70, 65 mm film, digital cinema, MTF, Nyquist, film grain, CMOS, human visual acuity, pixels per degree, MicroLED, Cinema LED, perceptual equivalence, film emulation

---

## Abstract

15/70 IMAX film has long been treated as a reference standard for large-format theatrical imaging. Its superiority, however, is often described using imprecise proxies such as the 1.43:1 aspect ratio, an alleged fixed “18K equivalent resolution,” or an assumed intrinsic infinitude of analog information. This manuscript reconstructs the problem from first principles as an end-to-end information channel: **scene → optics → photochemical or electronic capture → processing → master → projection/direct-view display → human visual system**.

Film is not an infinite-resolution continuum in any operational sense. Its useful information is bounded by lens point-spread functions, emulsion MTF, photon statistics, granularity, scattering, spectral sensitivities, processing chemistry, and the signal-to-noise ratio at a chosen contrast threshold. Consequently, no single K-value can uniquely represent 15/70 film resolution. Modern digital systems, meanwhile, separately demonstrate pixel density, sensor readout rates, large-area capture, high-bit-depth scanning, and emissive cinema display capabilities that approach or exceed the relevant spatial bandwidth of large-format film.

The central thesis is therefore not that digital cinema has already reproduced every phenomenological property of 15/70 IMAX, but that **the spatial-information advantage of 15/70 is no longer a fundamental digital impossibility**. The remaining problem is system integration and perceptual transfer-function equivalence: MTF/PSF, highlight behavior, spectral response, grain statistics, halation, temporal exposure, motion rendering, display flare, viewing geometry, and economics. A definitive comparison should be established by controlled psychophysical discrimination experiments rather than marketing resolution labels.

---

# 1. 연구 질문과 문제 재정의

## 1.1 표면 질문

대중적 질문은 보통 다음과 같이 제기된다.

1. IMAX의 1.43:1 화면비가 특별한가?
2. 15/70 필름은 정말 ‘18K’인가?
3. 최신 디지털 센서와 렌즈라면 같은 정보를 저장할 수 없는가?
4. 필름에는 LP·테이프 같은 아날로그 매체의 ‘실재감’이 존재하며, 그것은 디지털로 원리적으로 복제 불가능한가?
5. 삼성 같은 대형 디스플레이·반도체 기업이 충분히 투자하면 IMAX보다 높은 사양의 순수 디지털 시스템을 구축할 수 있는가?

이 다섯 질문은 사실 하나의 시스템 문제로 합쳐진다.

> **Q:** 15/70 IMAX 체인이 관객에게 전달하는 ‘지각 가능한 정보’를 현대 디지털 체인이 손실 없이 또는 지각적으로 구별 불가능한 수준으로 전달할 수 있는가?

## 1.2 화면비는 병목이 아니다

1.43:1은 기하학적 프레이밍 비율이다. 4:3(1.33:1) 텔레비전과 수치적으로 가깝지만, 그것이 IMAX의 기술적 본질은 아니다. 임의의 디지털 센서나 렌더러는 원하는 종횡비를 정의할 수 있다. 역사적 IMAX의 어려운 부분은 화면비 자체가 아니라 **거대한 네거티브 면적, 높은 투사 광량, 필름 이송 안정성, 거대 스크린에서의 MTF 유지, 정렬, 음향과 극장 지오메트리**였다.

즉, ‘1.43을 만들 수 있느냐’는 2026년에는 거의 문제가 아니다. 문제는 **1.43의 거대한 시야각을 채울 만큼 충분한 정보밀도를 종단 간 유지할 수 있느냐**이다.

## 1.3 본 논문의 판정 기준

본 논문은 세 수준을 분리한다.

- **물리적 동등성(physical identity):** 필름 유제와 디지털 센서가 같은 물질적 과정을 수행하는가? → 아니다.
- **신호 동등성(signal equivalence):** 관객에게 도달하기 직전의 광학 신호가 측정 허용오차 안에서 같은가? → 이론적으로 높은 수준까지 접근 가능하다.
- **지각적 동등성(perceptual equivalence):** 통제된 실험에서 인간 관객이 두 체인을 신뢰성 있게 구별할 수 있는가? → 실험으로 판정해야 한다.

중요한 것은 첫 번째가 달라도 세 번째가 성립할 수 있다는 점이다. 디지털은 필름과 ‘같은 물질’일 필요가 없다. **눈에 도달하는 신호의 차이가 인간의 판별 임계치 아래라면 지각적으로는 동등하다.**

---

# 2. 종단 간 영상 시스템의 제일원칙 모델

영화 화질은 카메라 센서의 K 숫자 하나로 결정되지 않는다. 단순화한 전달계는 다음과 같다.

```text
Scene radiance L(x,y,λ,t)
        ↓
Lens / optical PSF, flare, aberration, diffraction
        ↓
Capture medium
  ├─ Film: emulsion + chemistry + grain + spectral layers
  └─ Digital: CFA/RGBW + photodiode + charge + ADC + readout
        ↓
Image processing / scan / debayer / color transform / VFX / DI
        ↓
Distribution master / codec
        ↓
Projection or direct-view display
        ↓
Screen / room stray light / viewing geometry
        ↓
Human eye + retina + neural processing
        ↓
Perception
```

선형·시불변(LSI) 근사가 가능한 범위에서는 전체 공간주파수 응답을 대략 다음처럼 생각할 수 있다.

\[
MTF_{system}(f) \approx MTF_{lens}(f)\,MTF_{capture}(f)\,MTF_{processing}(f)\,MTF_{display}(f)\,MTF_{eye}(f)
\]

단, 필름은 노출에 따른 비선형성, 입자 통계, 현상 효과가 있고 디지털도 clipping·denoise·sharpening 등 비선형 처리가 존재하므로 이 식은 국소적(local) 근사다. 그래도 한 가지 사실을 매우 선명하게 보여준다.

> **전체 시스템의 정보량은 어느 한 요소의 최고 사양이 아니라 모든 단계의 합성 전달특성에 의해 결정된다.**

17K 센서 앞에 고주파 대비를 전달하지 못하는 렌즈를 달면 17K 파일에는 ‘17K개의 샘플’은 있지만 17K에 대응하는 장면 정보가 없다. 반대로 뛰어난 필름 네거티브를 저해상도 스캔·저광량 프로젝터로 내보내면 촬영단의 이점이 사라진다.

---

# 3. 15/70 IMAX가 역사적으로 강했던 이유

## 3.1 큰 프레임은 ‘아날로그 초고해상도 센서’ 역할을 했다

전통적인 대형 IMAX는 15-perforation 65 mm 카메라 네거티브와 70 mm 상영 프린트 체인을 사용한다. 일반 35 mm 프레임보다 훨씬 큰 면적을 사용하여 동일한 필름 입자 크기에서 더 많은 장면 정보를 담을 수 있다. 여기서 역사적 혁신은 간단하다.

> **작은 이미지를 더 크게 확대하는 대신, 원본 이미지 자체를 거대하게 만든다.**

디지털 센서·메모리·실시간 readout이 충분하지 않았던 시대에는 매우 합리적인 해법이었다. 센서 픽셀을 더 만들 수 없으니 감광 면적을 늘리고, 한 프레임의 물리적 크기를 키워 거대 스크린 확대 시 MTF와 grain visibility의 여유를 확보한 것이다.

## 3.2 1.43:1은 결과이지 핵심 발명품이 아니다

IMAX의 높은 세로 화면은 관객의 시야를 수직으로도 크게 채우며 몰입에 기여한다. 그러나 종횡비는 디지털 기술이 복제하기 어려운 물리적 속성이 아니다. 따라서 IMAX의 기술적 해자를 분석할 때 1.43:1 자체와 **대형 프레임 + 대형 스크린 + 근거리 관람 + 높은 영상 품질을 하나의 시스템으로 묶은 것**을 구별해야 한다.

## 3.3 ‘필름 면적’의 경제적 의미

대형 필름의 대가는 분명하다.

- 카메라와 매거진의 부피·중량 증가
- 필름 원재료·현상·검수 비용
- 짧은 롤 길이와 잦은 교체
- 카메라 기계소음
- 필름 이송과 게이트 안정성
- 고정밀 복사·프린트·영사 장비
- 물리적 마모·먼지·스크래치 관리

따라서 15/70은 ‘효율 최적화’가 아니라 **극한의 원본 품질을 위해 비용을 지불하는 시스템**이었다.

---

# 4. 필름은 무한해상도 아날로그 매체인가?

## 4.1 결론부터: 아니다

‘아날로그 = 연속 = 무한 정보’라는 직관은 실제 물리 시스템에는 적용되지 않는다. 필름은 좌표를 정수 픽셀 격자로 먼저 나누지 않는다는 의미에서 디지털 센서와 다르지만, 감광 유제 역시 유한 크기의 은염 결정, 염료 구름(dye cloud), 광자 수, 유제층 두께, 산란, 현상 반응을 갖는다.

즉 필름의 장면 정보에는 다음 한계가 존재한다.

1. 렌즈의 diffraction 및 aberration
2. 유제 내 광산란
3. 감광 입자·염료 구조의 확률성
4. 광자 shot noise
5. 노출과 현상에 따른 MTF 변화
6. 색층별 서로 다른 분광응답
7. granularity가 만드는 noise floor
8. 프린트·영사 과정에서의 추가 MTF 손실

필름은 픽셀이 없기 때문에 ‘정확히 몇 K’라고 말하기 어렵지만, **정보가 무한해서 K로 환산 불가능한 것은 아니다.** 더 정확하게는, MTF와 SNR의 연속 곡선을 하나의 숫자로 축약하기 때문에 K 환산이 본질적으로 문맥 의존적이다.

## 4.2 Kodak MTF가 보여주는 것

Kodak VISION3 50D 5203/7203의 기술문서는 필름 선명도를 MTF(Modulation Transfer Function)로 제시한다.[1] 공간주파수가 높아질수록 필름이 전달하는 대비는 점진적으로 감소한다. 즉 어느 지점에서 갑자기 ‘해상도가 끝나는’ 것이 아니라, 낮은 주파수의 높은 대비 정보에서 높은 주파수의 낮은 대비 정보로 연속적으로 쇠퇴한다.

따라서 다음 질문은 잘못된 질문이다.

> “이 필름은 몇 K인가?”

더 좋은 질문은 다음이다.

> “이 렌즈·필름·노출·현상 조합은 10, 20, 40, 80, 100 lp/mm에서 각각 얼마의 modulation을 유지하며, 그 신호가 grain/noise보다 충분히 높은가?”

## 4.3 고정된 ‘18K’ 표현의 한계

15/70 IMAX를 ‘18K급’으로 부르는 표현은 유용한 대중적 비유일 수 있으나 과학적 상수는 아니다. 15/70 이미지 폭을 공학적 사고실험상 약 70.4 mm로 두고 Nyquist 관계를 적용하면, 특정 공간주파수를 샘플링하기 위한 수평 샘플 수는 다음과 같다.

\[
N_x = 2 f W
\]

여기서 \(f\)는 lp/mm, \(W\)는 mm이다.

- 50 lp/mm → 약 7.0K samples
- 60 lp/mm → 약 8.4K
- 70 lp/mm → 약 9.9K
- 80 lp/mm → 약 11.3K
- 100 lp/mm → 약 14.1K
- 130 lp/mm → 약 18.3K

즉 ‘18K’는 대략 130 lp/mm 부근까지의 매우 미세한 구조를 샘플링한다는 가정과 대응할 수 있다. 그러나 그 주파수에서 **장면 대비가 얼마나 남아 있고 grain 대비보다 얼마나 큰가**를 묻지 않으면 숫자는 의미가 없다.

이것이 본 논문의 핵심 정정이다.

> **필름 해상도를 논할 때 K가 아니라 MTF × SNR × viewing condition을 봐야 한다.**

---

# 5. 렌즈 역시 무한 정보를 전달하지 않는다

ZEISS의 MTF 기술문서는 실제 렌즈가 점광원을 완벽한 수학적 점으로 재현하지 못하고 유한한 point spread function을 만든다는 사실을 설명한다.[2] diffraction, spherical aberration, coma, astigmatism, chromatic aberration, manufacturing tolerance, focus error 등은 고주파 정보를 제한한다.

이 점은 ‘최신 최고급 렌즈라면 디지털 센서가 다 받아먹을 수 있지 않느냐’는 질문을 정량화해 준다.

센서의 Nyquist 주파수는 픽셀피치 \(p\)에 대해 대략

\[
f_N = \frac{1}{2p}
\]

이다. Blackmagic URSA Cine 17K 65의 2.9 μm 픽셀피치를 적용하면[3]

\[
f_N \approx \frac{1}{2(0.0029)} \approx 172\;lp/mm
\]

이다.

이 값이 ‘카메라가 실제로 172 lp/mm의 장면 대비를 완벽히 기록한다’는 뜻은 아니다. CFA 구조, demosaic, OLPF 유무, 렌즈 MTF, photon noise가 존재한다. 그러나 매우 중요한 의미가 있다.

> **현대 시네마 센서의 샘플 격자는 이미 많은 시네마 렌즈가 의미 있는 대비를 전달하는 공간주파수보다 훨씬 촘촘하게 설계할 수 있다.**

따라서 2026년의 병목을 ‘디지털 픽셀이 너무 굵어서 최고급 렌즈 정보를 못 받는다’고 일반화하는 것은 맞지 않는다.

---

# 6. 2026년 디지털 캡처 기술이 이미 증명한 것

## 6.1 Blackmagic URSA Cine 17K 65

Blackmagic의 상용 URSA Cine 17K 65는 다음 사양을 제공한다.[3]

- 유효 센서: 50.81 × 23.32 mm
- 해상도: 17,520 × 8,040
- 약 141 MP
- 픽셀피치: 2.9 μm
- 동적범위: 16 stops
- 17K open-gate: 최대 60 fps
- 8 TB 내장 고성능 미디어 구성

이 카메라는 전통적 15/70 IMAX의 약 70 mm 폭 × 약 50 mm 높이를 그대로 갖는 센서는 아니다. 따라서 ‘이미 15/70을 완전히 대체했다’는 증거로 쓰면 안 된다.

하지만 다음을 실제 상용 제품으로 증명한다.

1. 1억 화소가 넘는 시네마 센서를 고속으로 읽을 수 있다.
2. 2.9 μm급 픽셀피치에서도 16-stop급 시네마 운용이 가능하다.
3. 17K급 RAW acquisition은 더 이상 연구실 개념이 아니다.
4. 65 mm급 광학 생태계와 실제 제작 workflow가 존재한다.

## 6.2 Canon 410 MP CMOS

Canon은 2025년 35 mm 풀프레임 면적에 24,592 × 16,704, 약 410 MP의 CMOS 센서를 발표했다.[5] 용도는 영화가 아니라 산업·의료·감시 분야이며, 따라서 이를 곧바로 ‘24K 시네마 카메라가 존재한다’고 해석하면 안 된다.

그럼에도 이 사례는 다른 질문에 답한다.

> **픽셀 자체를 수천만에서 수억 개로 고밀도 집적하는 것이 현재 반도체 공정에서 불가능한가? → 아니다.**

즉 15/70 대체의 어려움은 단순 픽셀 수가 아니라 **거대한 면적에서의 수율, 고속 병렬 readout, 발열, 전력, full-well capacity, 동적범위, 데이터 인터페이스를 동시에 만족시키는 것**이다.

## 6.3 ARRI ALEXA 265가 보여주는 반대편 증거

ARRI의 ALEXA 265는 오히려 ‘해상도 숫자만 올리는 것’이 영화 화질의 목적함수가 아님을 보여준다. ARRI는 사용자 피드백에 따라 6.5K 해상도와 큰 픽셀피치를 유지하면서 ALEXA 65 대비 동적범위를 14 → 15 stops로, 감도를 개선하는 방향을 택했다고 밝힌다.[4]

이는 매우 중요하다.

> **충분한 공간 샘플링을 확보한 뒤에는 추가 K보다 DR, noise floor, highlight behavior, color, low-light, lens rendering이 더 높은 한계효용을 가질 수 있다.**

따라서 ‘디지털 IMAX killer’는 30K 센서를 만드는 프로젝트가 아니라, **필요한 공간 대역폭을 넘긴 뒤 나머지 전달함수를 최적화하는 프로젝트**여야 한다.

---

# 7. 필름을 디지털로 ‘저장’하는 기술은 있는가?

## 7.1 이미 있다

Lasergraphics Director는 최대 13.5K 스캔, IMAX/VistaVision 및 65/70 mm 지원, sequential RGB 방식의 full-color-per-pixel 취득, HDR 다중노출 스캔을 제공한다.[6] 이것은 중요한 실증이다.

> **15/70 필름에 기록된 광학 밀도 패턴을 고해상도 디지털 데이터로 변환하는 기술은 이미 존재한다.**

물론 ‘13.5K scanner가 필름의 모든 가능한 미시적 입자 정보를 100% 보존한다’고 단정할 수는 없다. 스캐너 자체의 렌즈 MTF, sampling aperture, focus, flare, noise, bit depth가 존재한다. 하지만 ‘아날로그 필름은 디지털로 원리적으로 저장할 수 없다’는 주장과는 전혀 다른 현실이다.

## 7.2 중요한 것은 oversampling과 noise floor

어떤 아날로그 매체를 디지털화할 때 목표는 수학적 연속체를 무한 정밀도로 복사하는 것이 아니다. 목표는 다음이다.

1. 매체의 유효 신호 대역보다 높은 sampling bandwidth 확보
2. 매체의 유효 동적범위보다 낮은 quantization/noise floor 확보
3. 스캐너 자체의 MTF가 원본보다 충분히 높을 것
4. 색층 및 밀도 특성을 충분히 측정할 것

이 조건을 만족하면 더 높은 샘플레이트가 만들어내는 추가 데이터 대부분은 **새로운 장면 정보가 아니라 grain/noise의 더 정밀한 기술(description)**이 된다.

---

# 8. 아날로그 필름의 ‘느낌’은 실제로 존재하는가?

## 8.1 존재한다. 그러나 ‘무한 정보’와는 다른 문제다

필름과 디지털은 같은 장면을 찍어도 기본 transfer function이 다르다. 필름 특유의 시각적 성격에는 다음이 포함된다.

- 노출-밀도 곡선의 toe와 shoulder
- highlight에서의 점진적 압축
- 유제 내부 산란에 의한 halation
- 색층별 분광 감도와 층간 상호작용
- grain의 공간적 power spectrum
- 노출 밀도에 따라 달라지는 grain visibility
- 프레임마다 새로 형성되는 시간적 grain randomness
- 현상 과정에서의 국소 대비 변화
- 프린트 및 투사 광학의 flare/veiling glare
- 렌즈와 필름 MTF의 곱으로 생기는 microcontrast

따라서 ‘17K로 찍으면 자동으로 필름처럼 보인다’는 주장은 틀리다.

## 8.2 필름 에뮬레이션은 LUT 하나가 아니다

진정한 필름 동등성을 목표로 한다면 디지털 변환은 최소한 다음 형태여야 한다.

\[
I_{out}=F(I_{scene},\lambda,x,y,t,E,stock,process,lens,projection)
\]

단순 3D LUT는 주로 색과 톤의 정적 변환을 다룬다. 그러나 필름 grain은 공간·시간·노출 의존 확률과정이고, halation은 주변 픽셀과 상호작용하는 공간 연산이며, MTF는 주파수 의존적이다.

따라서 정교한 필름 모델은 다음을 포함해야 한다.

1. **Sensitometric response** — 노출 대비 밀도 곡선
2. **Spectral response** — 색층별 파장 감도
3. **Spatial operator** — PSF/MTF, diffusion, halation
4. **Stochastic model** — density-conditioned grain distribution
5. **Temporal model** — 프레임 간 grain 독립성/상관성
6. **Cross-channel covariance** — RGB층 grain의 상호관계
7. **Projection model** — 프린트 MTF, 광원, flare, black floor

이 전체를 모델링해야 ‘아날로그 느낌’을 물리적으로 논할 수 있다.

## 8.3 Grain은 항상 더 좋은가?

그렇지도 않다. 2024년 *Electronic Imaging*의 film-grain 사용자 선호 연구는 일부 정지영상 조건에서 film-grain이 Gaussian noise보다 선호되는 조건을 관찰했지만, 전반적으로 낮은 noise가 선호되었고 영상 시퀀스에서는 noise-free 조건이 grain 조건보다 선호되는 결과도 보고했다.[12]

따라서 다음 두 주장을 동시에 피해야 한다.

- “grain은 그냥 결함이므로 없앨수록 무조건 좋다” → 과도한 단순화
- “사람은 본질적으로 film grain을 더 좋아한다” → 근거 부족

더 정확한 결론은 **grain은 미학적·지각적 신호이며, 선호도는 콘텐츠와 세기, 관람조건에 따라 달라진다**이다.

---

# 9. 오디오 아날로그와 영상 필름의 비교

## 9.1 유효한 비유

하이엔드 아날로그 오디오 경험에서 중요한 직관은 옳다.

> **샘플레이트를 올린다고 ‘실재감’이 자동으로 생기지 않는다.**

오디오에서 실제 결과는 마이크, 프리앰프, 트랜스포머, 테이프, 커팅헤드, groove, 카트리지, 앰프, 스피커, 룸의 전달함수가 합성된 것이다. 영상도 렌즈, 필름/센서, 현상/processing, display가 합쳐진 결과다.

따라서 오디오의

> “192 kHz니까 더 자연스럽다”

와 영상의

> “17K니까 더 필름 같다”

는 같은 종류의 범주 오류다.

## 9.2 LP에 대한 물리적 정정

LP의 all-analog chain은 디지털 샘플링을 거치지 않을 수 있지만, 신호가 처음부터 끝까지 ‘전기’ 상태로 저장되는 것은 아니다. 마이크에서 전기 신호가 된 후 커팅헤드는 이를 **기계적 groove 변위**로 변환하고, 재생 시 stylus의 기계 운동을 카트리지가 다시 전기 신호로 변환한다. RIAA equalization, cutter/stylus geometry, tracking error, resonance, distortion 등이 체인의 일부다.

즉 LP의 매력은 ‘무한한 연속성’ 하나보다 **특정한 아날로그 전달함수와 비선형성**에 더 가깝다.

## 9.3 고해상도 오디오 연구가 말하는 것

Reiss의 2016년 AES 메타분석은 18개 실험, 400명 이상, 12,500회 이상의 trial을 종합하여 고해상도 오디오와 CD급 오디오 사이에 작지만 통계적으로 유의한 판별 가능성을 보고했으며, 훈련된 청취자에서 효과가 커졌다.[11]

이 결과는 ‘아날로그가 디지털보다 우월하다’를 증명하지 않는다. 그러나 **지각 임계치를 너무 쉽게 가정해서도 안 된다**는 교훈을 준다. 영상에서도 ‘60 ppd 넘으면 아무도 절대 못 본다’ 같은 단정 대신 실제 psychophysics가 필요하다.

## 9.4 영상 쪽이 더 쉽게 닫히는 부분

영상은 공간 좌표와 시야각을 통해 sampling density를 ppd로 직접 환산하기 쉽고, 인간 눈의 공간분해능을 실험적으로 측정할 수 있다. 따라서 특정 좌석·스크린 크기에서 ‘더 높은 K가 지각 가능한가’를 비교적 직접 계산할 수 있다.

하지만 색, 운동, 밝기, 눈의 적응, peripheral vision까지 들어가면 영상 역시 단순하지 않다. **공간해상도 하나로 perceptual completeness를 선언해서는 안 된다.**

---

# 10. 인간 시각은 실제로 몇 K를 요구하는가?

## 10.1 60 ppd는 절대 상수가 아니다

오랫동안 20/20 시력을 1 arcminute 기준으로 환산한 약 60 ppd가 ‘retina resolution’처럼 사용되었다. 그러나 Ashraf, Chapiro, Mantiuk의 2025년 *Nature Communications* 연구는 중심와 무채색 조건에서 약 94 ppd에 이르는 분해능을 측정했고, 색축과 eccentricity에 따라 다른 한계를 보고했다.[7]

따라서 고급 극장 설계에서 60 ppd를 절대 상한으로 쓰는 것은 보수적이지 않을 수 있다.

## 10.2 시야각 기반 계산

스크린 수평 해상도 \(N\), 관객에게 보이는 수평 시야각 \(\theta\)에 대해 단순 평균 ppd는

\[
PPD \approx \frac{N}{\theta}
\]

이다.

예시:

- 4K(4096) / 100° ≈ 41 ppd
- 8K(8192) / 100° ≈ 82 ppd
- 9.4K / 100° ≈ 94 ppd
- 12K(12,288) / 100° ≈ 123 ppd

따라서 100°에 가까운 매우 넓은 좌석에서는 4K가 충분히 조밀하지 않으며, 8K도 매우 좋은 중심와 시력 기준에서는 차이가 남을 수 있다. 반면 12K는 100°에서 약 123 ppd이므로 상당히 보수적인 상한에 접근한다.

## 10.3 FOV별 필요한 수평 해상도

94 ppd를 기준으로 보면:

- 50° → 약 4.7K
- 60° → 약 5.6K
- 70° → 약 6.6K
- 80° → 약 7.5K
- 90° → 약 8.5K
- 100° → 약 9.4K
- 110° → 약 10.3K

120 ppd의 매우 높은 기준을 적용하면:

- 80° → 9.6K
- 90° → 10.8K
- 100° → 12.0K
- 110° → 13.2K

이 표에서 중요한 것은 ‘12K가 정답’이 아니라 **K 요구량은 스크린 폭이 아니라 시야각과 관객 시력으로 결정된다**는 점이다.

## 10.4 중심와와 주변시의 차이

한 프레임 전체를 동시에 94~120 ppd로 보는 것은 아니다. 인간의 최고 해상도는 중심와 주변의 좁은 영역에 집중되어 있고 eccentricity가 커지면 분해능은 감소한다. 다만 영화 관객은 화면의 여러 위치로 눈을 움직이므로 **어느 위치든 순간적으로 중심와가 될 수 있다.** 따라서 대형 스크린 전체에 높은 픽셀밀도를 제공하는 것은 의미가 있지만, 그 이득은 좌석과 장면에 따라 달라진다.

---

# 11. 상영 기술: 프로젝션의 한계와 Direct-View의 전환

## 11.1 디지털 시네마 표준 자체가 이미 Direct View를 인정한다

Digital Cinema Initiatives(DCI)는 2026년 Digital Cinema System Specification v1.5.0을 운영하고 있으며, 별도의 HDR D-Cinema Addendum과 Direct View Display Addendum을 제공한다.[8] 즉 극장 영상의 미래가 반드시 ‘프로젝터 → 반사 스크린’이어야 한다는 전제 자체가 표준 차원에서 이미 깨졌다.

## 11.2 Samsung Onyx 2026

삼성의 2026년형 Onyx Cinema LED는 다음 특성을 제시한다.[9]

- 14 m 표준 모델
- 최대 4K, 120 Hz
- 14 m 모델 3.3 mm pixel pitch
- 20 m까지 확장
- 최대 300 nit
- 직접발광형 구조

여기서 중요한 것은 300 nit 자체보다 **프로젝션 광학계를 제거한다**는 점이다. Direct View는 projection lens, screen reflectance, projector black leakage의 일부 문제를 제거하고, 각 픽셀을 직접 발광시킨다.

## 11.3 ‘30 m 12K’는 픽셀피치 관점에서 SF가 아니다

12K를 12,288 pixels로 두면 30 m 폭에서 필요한 pixel pitch는

\[
p = \frac{30,000\;mm}{12,288}\approx2.44\;mm
\]

이다.

이는 현재 삼성 Onyx 10 m 계열의 약 2.5 mm pitch와 같은 자릿수다. 즉 **픽셀을 그만큼 작게 만드는 것 자체가 미래 기술이 아니다.**

20 m 폭 12K라면

\[
p\approx1.63\;mm
\]

이다. 이 또한 오늘날 대형 LED 제조기술의 물리적 불가능 영역이 아니라 비용·수율·모듈 수·전력·보정의 문제다.

## 11.4 Direct View의 새로운 문제

프로젝터를 제거하면 모든 문제가 사라지는 것은 아니다.

- 수백 m²에 달하는 모듈의 색/휘도 균일도
- aging drift와 pixel failure
- seam visibility
- 전력 및 열관리
- viewing-angle color shift
- calibration 유지
- 카메라/콘텐츠의 black level과 display black의 불일치
- 기존 극장의 음향 구조

특히 전통적 영화관은 대사 localization을 위해 screen behind loudspeaker 구성을 사용한다. 불투명한 LED wall은 이 구조를 그대로 사용할 수 없으므로 **영상 시스템을 바꾸면 음향 아키텍처도 함께 다시 설계해야 한다.** 이것은 ‘삼성이 패널만 크게 만들면 끝’이라는 주장에 대한 중요한 반례다.

---

# 12. ‘Digital 15/70 Superset’의 제안 사양

본 절은 존재하는 제품을 기술하는 것이 아니라 **현재 입증된 부품기술을 조합했을 때 가능한 연구용 목표 사양**을 제안한다.

## 12.1 Capture Sensor

15/70의 1.43 상영영역에 대응하는 사고실험으로 약 70.4 mm 수평 폭과 약 49.2 mm 높이를 사용한다. 정확한 카메라/프린트 aperture는 시스템과 crop에 따라 달라질 수 있으므로 여기서는 계산을 위한 명시적 가정이다.

### Option A — 12K sensor

- 12,288 × 약 8,593 (1.43:1)
- 약 105.6 MP
- 70.4 mm 폭 기준 pixel pitch ≈ 5.73 μm
- Nyquist ≈ 87 lp/mm

### Option B — 14.1K sensor

- 약 14,082 × 9,848
- 약 138.7 MP
- pixel pitch ≈ 5.0 μm
- Nyquist ≈ 100 lp/mm

Option B는 Kodak 50D 같은 저입자 필름의 상당한 고주파 응답을 넉넉하게 oversample하는 연구목표로 유용하다. 18K는 더 높은 주파수 tail/grain까지 보수적으로 샘플링하는 archive-oriented 목표로 볼 수 있지만, **극장 관객에게 18K delivery가 반드시 필요하다는 결론은 나오지 않는다.**

## 12.2 Dynamic Range 및 readout

목표:

- 최소 현재 최상급 대형 시네마 수준의 DR; 연구 목표 16-stop급 이상
- global shutter 또는 film rotary shutter와 지각적으로 매칭 가능한 temporal integration
- 높은 full-well capacity
- dual-gain 또는 multi-gain readout 검토
- low fixed-pattern noise
- 고정밀 온도 보정
- 16-bit container 또는 충분한 ENOB를 보장하는 high-bit-depth RAW

여기서 ‘16 bit’와 ‘16 stops’는 전혀 다른 개념이다. ADC container bit depth가 높아도 센서 noise가 크면 유효 비트수는 낮다.

## 12.3 Optical System

렌즈는 단순 ‘8K/12K 대응’ 마케팅 라벨이 아니라 다음 데이터로 선별해야 한다.

- sagittal/tangential MTF
- 10/20/40/80/100 lp/mm response
- field position별 MTF
- focus breathing
- longitudinal/lateral chromatic aberration
- veiling glare
- flare characteristic
- distortion
- spectral transmission

궁극적으로는 **렌즈 MTF와 센서 sampling aperture를 함께 측정한 system MTF**가 필요하다.

## 12.4 Color 및 spectral calibration

필름과 디지털의 색 차이는 단순 white balance 문제가 아니다. 서로 다른 spectral sensitivity를 가진 두 카메라는 동일한 XYZ 색에 대해 조명 SPD에 따라 다른 sensor response를 만들 수 있다.

따라서 필름 등가성을 목표로 한다면:

1. 필름 색층의 spectral sensitivity 측정
2. 디지털 CFA/RGBW spectral sensitivity 측정
3. tungsten/daylight/LED/laser 등 다양한 illuminant SPD에서 color error 측정
4. skin, fabric, foliage, saturated pigments에 대한 metamerism 테스트
5. 단일 LUT가 아니라 illuminant-aware color transform 검토

가 필요하다.

## 12.5 Processing Pipeline

권장 연구 파이프라인:

```text
12–14K high-bit-depth RAW
→ sensor calibration
→ scene-referred linear representation
→ lens/optics metadata
→ optional film-transfer model
→ VFX / compositing at resolution-preserving workflow
→ 12K archival master
→ seat/FOV-dependent 12K/8K/4K theatrical derivatives
→ Direct View / laser projection variants
```

핵심은 camera sharpening이나 denoise를 초기에 강하게 bake-in하지 않는 것이다. 원시 장면 신호를 보존하고, 최종 전달함수는 후단에서 제어해야 한다.

---

# 13. 데이터량: 기술적 불가능인가, 경제적 문제인가?

## 13.1 14.1K, 1.43:1, 16-bit 단일 RAW sample 계산

138.7 MP × 2 bytes × 24 fps:

\[
\approx6.66\;GB/s
\]

시간당:

\[
6.66\times3600\approx24\;TB/h
\]

60 fps라면 약 16.6 GB/s, 약 60 TB/h가 된다.

12-bit packed라면 이론적 raw payload는 더 줄어든다. 실제 cinema RAW는 무손실 또는 시각적 무손실 압축을 사용할 수 있다.

## 13.2 이 숫자의 의미

24 TB/h는 소비자 장비에는 크지만 현대 영화 제작·데이터센터 관점에서 ‘자연법칙상 불가능’한 수치가 아니다. 더 큰 문제는 저장장치 하나가 아니라 다음 전체 비용이다.

- 촬영 원본 복제 3개 이상
- on-set offload
- 네트워크 전송
- editorial proxy
- VFX plates
- render farm I/O
- color grading
- archive checksum 및 LTO/object storage
- 극장용 delivery master

즉 병목은 **storage physics → workflow economics**로 이동했다.

---

# 14. 왜 해상도만 올려서는 ‘실재감’이 생기지 않는가

## 14.1 디지털의 ‘차갑고 날카로운’ 느낌의 가능한 원인

고해상도 영상이 필름보다 차갑게 느껴지는 경우, 원인을 sampling 자체에만 귀속하면 안 된다. 가능한 원인은 다음과 같다.

- edge enhancement / oversharpening
- local contrast enhancement
- digital clipping
- 너무 깨끗한 temporal noise profile
- rolling-shutter motion
- aggressive denoise 후 texture reconstruction
- 좁거나 다른 spectral response
- lens choice
- high microcontrast coatings
- display의 매우 낮은 black과 높은 local contrast
- film projection에 존재하던 flare/halation 부재

즉 더 높은 resolution은 **있는 전달특성을 더 정확히 보여줄 뿐**, 그 전달특성 자체를 필름으로 바꾸지 않는다.

## 14.2 역설: 더 좋은 디스플레이는 필름을 덜 닮을 수 있다

극도로 깊은 black을 가진 MicroLED에서 15/70 필름 스캔을 그대로 재생하면 실제 필름 영사보다 contrast가 높아 보일 수 있다. 전통적 영사는 projector flare, screen scatter, room stray light로 black floor가 올라간다.

따라서 ‘필름과 같아지기’가 목표라면 더 좋은 디스플레이에서 오히려 일부 특성을 **의도적으로 모델링**해야 할 수 있다.

이것은 매우 중요한 통찰이다.

> **재현 장치의 물리 성능이 원본 매체보다 높을수록, 원본의 제한까지 정확히 시뮬레이션할 자유가 생긴다.**

즉 고성능 디지털 장치는 필름의 한계를 강제로 갖는 것이 아니라 필요할 때 선택적으로 재현할 수 있다.

---

# 15. 필름과 디지털을 가르는 진짜 미해결 영역

## 15.1 Sensor size와 수율

70 × 50 mm급 센서는 일반적인 단일 노광 reticle보다 매우 크다. 대형 die는 결함 확률과 wafer 수율에서 불리하고 stitching, alignment, readout partition이 필요할 수 있다. 따라서 ‘삼성이 반도체 회사니까 그냥 큰 센서 만들면 된다’는 말은 방향은 맞아도 비용을 과소평가한다.

하지만 이것은 **가능/불가능의 경계가 아니라 yield curve와 가격의 문제**다.

## 15.2 Full-well capacity와 픽셀피치

픽셀을 작게 만들수록 일반적으로 하나의 photodiode가 저장할 수 있는 전자 수, 즉 full-well capacity에 불리할 수 있다. 큰 센서에서 무작정 30K를 추구하면 DR·감도·read noise와 trade-off가 생긴다.

따라서 12–14K × 5–6 μm급 접근은 ‘최대 K’보다 **공간해상도와 photon capacity의 균형**을 노리는 설계다.

## 15.3 Readout과 열

1억 화소 이상을 24–60 fps, high bit depth로 읽으면 센서와 주변 ASIC에서 막대한 데이터가 발생한다. 열은 dark current, fixed-pattern noise, calibration drift에 영향을 준다. 냉각은 카메라 크기·소음·전력과 연결된다.

## 15.4 VFX가 진짜 병목이 될 수 있다

카메라가 14K여도 VFX asset, texture, simulation, compositing, render가 4K/8K에서 이루어지면 final master의 실제 정보대역은 중간단에서 제한된다.

따라서 ‘14K camera’를 만드는 것보다 **14K가 끝까지 살아남는 production pipeline**을 만드는 것이 더 어렵고 비쌀 수 있다.

## 15.5 극장 경제성

대형 LED wall은 다음 비용을 발생시킨다.

- 초기 CAPEX
- module replacement inventory
- calibration labor
- cooling/HVAC
- 전력
- theater rebuild
- audio redesign
- content mastering

그러므로 삼성·LG·Sony급 회사가 기술적으로 만들 수 있다는 것과, 전 세계 수천 개 극장에 경제적으로 설치할 수 있다는 것은 다른 질문이다.

---

# 16. 결정적 검증 실험: ‘보이는가?’를 직접 측정하라

논쟁을 끝내는 방법은 간단하다. ‘18K냐 12K냐’를 인터넷에서 싸우는 것이 아니라 **사람에게 보여주고 통계적으로 판별 가능한지 측정**하면 된다.

## 16.1 연구 목표

### Experiment A — Exhibition equivalence

같은 15/70 original negative를 두 경로로 상영한다.

- A1: photochemical print → calibrated 15/70 projector
- A2: 최고급 13.5K 이상 scan → high-bit-depth digital master → 12K direct-view 또는 동급 display

목표: **캡처 매체를 동일하게 두고 상영 체인만 비교**한다.

### Experiment B — Capture equivalence

동일 장면을 최대한 동시·동일 조건으로 촬영한다.

- B1: 15-perf 65 mm film negative
- B2: 12–14K, 약 70 × 50 mm class digital prototype

동일 lens family, matched field of view, matched exposure time, matched depth of field, 동일 조명을 사용한다.

B2에는 두 조건을 둔다.

- B2-Raw: 디지털 기본 rendering
- B2-FilmModel: 측정 기반 film transfer model 적용

## 16.2 자극(scene) 설계

단순 해상도 차트만으로는 부족하다. 최소 다음 장면이 필요하다.

1. 미세 섬유·머리카락·피부
2. 나뭇잎·풀·모래 등 stochastic texture
3. 고대비 backlight와 specular highlights
4. neon/LED/laser 등 특이한 SPD
5. tungsten skin tone
6. 저조도 암부
7. 안개·연무·flare
8. 빠른 카메라 pan
9. 빠른 피사체 motion
10. 깊은 심도와 얕은 심도 각각
11. saturated color patches
12. 별·야경처럼 작은 고대비 point sources

## 16.3 측정 장비

주관평가만 하지 않고 동시에 다음을 측정한다.

- system MTF / slanted edge
- point spread function
- spectral sensitivity
- scene-referred DR
- noise power spectrum
- grain spatial power spectrum
- temporal noise autocorrelation
- color difference under multiple illuminants
- highlight roll-off
- flare/veiling glare
- display luminance uniformity
- black floor
- seat별 PPD/FOV

## 16.4 Psychophysics

### 판별과 선호를 분리

두 질문은 다르다.

1. **Discrimination:** 어느 것이 필름인지 맞힐 수 있는가?
2. **Preference:** 어느 쪽을 더 선호하는가?

필름을 구별할 수 있어도 디지털을 더 좋아할 수 있고, 반대도 가능하다.

### 실험 방식

- randomized double blind
- 2AFC 또는 ABX
- 동일 scene pair 반복
- trained cinematographers/colorists 그룹
- 일반 관객 그룹
- 좌석/FOV 층화
- 시력 검사 및 교정시력 기록
- 사전등록된 분석계획
- 파일명·영사기 소리·교체시간 등 cue 제거

ABX에서 signal detection metric을 사용하면

\[
d' = z(Hit) - z(FalseAlarm)
\]

같은 형태로 단순 정답률보다 민감하게 판별능력을 분석할 수 있다. ‘구별 못함’을 증명하기 위해서는 단순한 비유의성(p>0.05)이 아니라 **사전에 정한 equivalence margin을 이용한 등가성 검정**이 필요하다.

## 16.5 반증 가능성

본 논문의 가설은 다음 결과가 나오면 틀린다.

> 충분히 높은 spatial sampling, DR, color calibration, film-transfer model, display calibration을 모두 적용했는데도 훈련된 관객과 일반 관객이 여러 콘텐츠·좌석 조건에서 일관되고 재현 가능하게 15/70 photochemical chain을 판별하며, 그 차이가 측정 가능한 아직 모델링되지 않은 물리 변수를 추적한다면 ‘지각적 대체 가능’ 가설은 기각 또는 수정되어야 한다.

반대로 다음 결과가 반복되면 ‘필름의 원리적 디지털 비복제성’ 주장은 약해진다.

> 통제된 실험에서 차이를 유의하게 판별하지 못하고, 더 높은 해상도나 더 정교한 film model을 추가해도 판별능력이 chance 부근에 머문다면 디지털은 해당 관람조건에서 15/70과 지각적으로 동등하다고 볼 근거가 생긴다.

---

# 17. 삼성 같은 기업이 실제로 만들 수 있는가?

## 17.1 필요한 기술의 소유 구조

가상의 프로젝트를 ‘Samsung Digital Large Format Cinema’라고 부르자. 필요한 서브시스템은 다음과 같다.

### 반도체

- 초대형 stitched CMOS
- high-speed column ADC
- 12–16 bit class readout architecture
- advanced packaging
- thermal management

### 디스플레이

- MicroLED/Cinema LED
- 1.5–2.5 mm class pixel pitch at 20–30 m scale
- module-level calibration
- 12K controller
- high-bit-depth HDR drive

### 저장/컴퓨팅

- 50–200 Gbit/s class on-camera internal fabric depending compression
- NVMe/flash RAID
- high-speed networking
- GPU/NPU based 12K image processing

### 광학/카메라

삼성이 모든 것을 직접 만들 필요도 없다. 대형포맷 렌즈는 ARRI/ZEISS/Leitz/Panavision 계열 생태계와 협업할 수 있고, 카메라 플랫폼은 전문 제조사와 공동개발할 수 있다.

## 17.2 가장 어려운 것은 기술 하나가 아니라 ‘제품화’다

현재 공개된 기술을 보면 다음 각각은 이미 입증됐다.

- 17K 65 mm급 시네마 촬영 → 존재
- 24K급 픽셀 수의 풀프레임 CMOS → 존재
- 13.5K IMAX film scan → 존재
- 20 m Cinema LED → 존재
- 300 nit theatrical direct view → 존재

그러나 다음 통합제품은 아직 일반적인 상용 표준이 아니다.

> **70 × 50 mm class 12–14K cinema capture + 12K DI/VFX + 20–30 m 12K 1.43 direct-view + photochemical-equivalent transfer model + standardized distribution**

따라서 가장 정확한 표현은 다음이다.

> **‘못 만드는 기술’이라기보다 ‘아직 한 사업자가 종단 간 제품으로 묶어 경제성을 입증하지 않은 기술’에 가깝다.**

---

# 18. IMAX의 진짜 해자는 무엇인가?

기술을 픽셀 수로만 보면 IMAX의 해자가 약해 보인다. 그러나 사업 시스템으로 보면 여전히 강하다.

IMAX는 단순 카메라 회사가 아니라 다음을 묶는다.

- 촬영 포맷과 인증
- filmmaker 관계
- post/mastering
- 배급
- projector/display 규격
- 스크린과 좌석 geometry
- 음향
- theater QA
- 브랜드
- 관객의 ‘IMAX면 더 크고 좋다’는 신뢰

즉 2026년 IMAX의 방어력은 필름 유제의 물리법칙 하나가 아니라 **end-to-end standardization과 network effect**다.

삼성이 더 좋은 패널을 만든다고 자동으로 IMAX를 이기는 것이 아니다. 콘텐츠 제작자가 그 포맷으로 촬영·마스터하고, 배급사가 보내고, 극장이 설치하고, 관객이 추가 요금을 낼 이유가 있어야 한다.

---

# 19. 주요 명제의 확정·추론·미확정 구분

## 19.1 높은 확신으로 확인되는 사실

1. 필름은 고정된 ‘K 해상도’를 갖지 않고 MTF/SNR로 다루는 것이 더 정확하다.
2. 실제 렌즈의 MTF는 유한하다.
3. 17K급 65 mm 디지털 시네마 카메라는 상용화되어 있다.
4. 410 MP/24K급 픽셀밀도의 CMOS는 시연되어 있다.
5. IMAX/65/70 mm 필름의 13.5K급 디지털 스캔 장비가 존재한다.
6. 20 m급 Cinema LED와 300 nit급 직시형 시네마가 존재한다.
7. 인간 중심와 해상도는 전통적인 60 ppd보다 높은 조건이 실험적으로 보고됐다.

## 19.2 강한 공학적 추론

1. 15/70의 유효 공간정보를 충분히 oversample하는 12–14K급 초대형 디지털 센서는 현재 기술 계열의 확장선상에 있다.
2. 20–30 m, 12K direct-view display는 pixel pitch 자체보다 비용·수율·전력·보정이 병목이다.
3. 15/70의 공간해상도 우위는 더 이상 ‘디지털이 원리적으로 접근할 수 없는 영역’이 아니다.
4. 필름 look의 남는 차이는 주로 transfer-function difference이며, 단순 K가 아니다.

## 19.3 아직 실험 없이 확정할 수 없는 것

1. 모든 종류의 장면에서 12–14K digital이 15/70 film과 지각적으로 완전히 동등한가?
2. 훈련된 촬영감독·컬러리스트가 블라인드 조건에서 일관되게 차이를 구별할 수 있는가?
3. film spectral response와 grain/halation을 어느 정도 모델링해야 판별이 사라지는가?
4. 8K, 10K, 12K, 14K 중 실제 IMAX 좌석에서 경제적 최적점은 어디인가?
5. direct-view의 높은 contrast가 전통적 projection과 다른 ‘디지털 느낌’을 얼마나 만드는가?

이 질문은 논리로 답할 수 없고 실험해야 한다.

---

# 20. 결론

본 연구는 15/70 IMAX를 ‘아날로그이므로 무한한 디테일을 담는 신비한 매체’로 보는 관점과, 반대로 ‘17K 센서만 있으면 이미 완전히 끝난 기술’로 보는 관점을 모두 거부한다.

15/70 IMAX의 역사적 위대함은 분명하다. 디지털 센서와 저장장치가 작은 시대에 **거대한 광화학 프레임을 사용하여 장면의 공간정보를 물리적으로 대량 저장하고, 그것을 거대한 스크린까지 유지하는 종단 간 시스템**을 구축했다. 당시에는 매우 공격적이고 합리적인 공학이었다.

그러나 2026년의 조건은 다르다.

- 픽셀밀도는 17K 시네마 및 24K급 센서 수준까지 올라왔다.
- 대형 디지털 센서는 이미 65 mm급 상용 제품이 존재한다.
- 필름은 13.5K급으로 스캔할 수 있다.
- 20 m급 직시형 Cinema LED가 존재한다.
- 인간 시각 한계는 ppd와 FOV로 정량화할 수 있다.

따라서 현대의 질문은

> “디지털이 필름만큼 잘게 쪼갤 수 있는가?”

가 아니다.

더 정확한 질문은

> **“필름의 유효 공간정보와 비선형·확률적 전달특성을 디지털이 인간의 판별 임계치 아래까지 측정·모델링·재생할 수 있는가?”**

이다.

본 논문의 판단은 **가능성이 높다**이다. 그러나 이 결론은 ‘아날로그와 디지털은 똑같다’는 철학적 주장에 의존하지 않는다. 필름도 렌즈도 인간의 눈도 유한한 대역폭과 noise floor를 가진 실제 물리계이고, 디지털 시스템은 그 유효 출력보다 충분히 높은 sampling density와 dynamic range를 확보할 수 있다는 사실에 의존한다.

남은 결정적 문제는 세 가지다.

1. **Integration** — 대형 센서부터 12K 극장까지 하나의 안정적 체인으로 묶는 것
2. **Transfer-function equivalence** — film MTF, grain, spectral response, halation, highlight, motion을 모델링하는 것
3. **Economics** — 관객이 구별하거나 가치를 느끼는 개선에만 비용을 쓰는 것

따라서 차세대 대형 시네마의 올바른 목표는 ‘18K’라는 숫자를 이기는 것이 아니다.

> **장면에서 인간 지각까지의 모든 병목을 측정하고, 관객이 더 이상 원본 15/70 체인과 구별하지 못하는 최소 충분 사양을 찾아내는 것.**

그 지점이 진짜 디지털 IMAX의 완성점이다.

---

# 부록 A. 15/70 폭 가정에서 공간주파수별 필요한 수평 샘플 수

계산 가정: 이미지 폭 W = 70.41 mm, Nyquist 기준 2 samples/cycle.

| 공간주파수 | 수평 샘플 수 |
|---:|---:|
| 10 lp/mm | 1,408 |
| 20 lp/mm | 2,816 |
| 30 lp/mm | 4,225 |
| 40 lp/mm | 5,633 |
| 50 lp/mm | 7,041 |
| 60 lp/mm | 8,449 |
| 70 lp/mm | 9,857 |
| 80 lp/mm | 11,266 |
| 100 lp/mm | 14,082 |
| 130 lp/mm | 18,307 |

**해석 주의:** Nyquist 샘플 수는 alias-free sampling의 이상적 최소 관계이지, 해당 주파수에서 실제 렌즈·필름이 충분한 contrast/SNR을 갖는다는 보증이 아니다. 실제 시스템은 sampling aperture, CFA, demosaic 및 anti-aliasing을 고려해 oversampling margin이 필요하다.

---

# 부록 B. 극장 시야각별 해상도 요구량

| 수평 FOV | 94 ppd 기준 | 120 ppd 기준 |
|---:|---:|---:|
| 50° | 4.7K | 6.0K |
| 60° | 5.6K | 7.2K |
| 70° | 6.6K | 8.4K |
| 80° | 7.5K | 9.6K |
| 90° | 8.5K | 10.8K |
| 100° | 9.4K | 12.0K |
| 110° | 10.3K | 13.2K |

이 계산은 해상도만을 고려한 상한 분석이다. 실제 지각은 contrast, luminance, eccentricity, motion, accommodation, 개인 시력에 따라 달라진다.

---

# 부록 C. 제안하는 검증 체크리스트

## Capture

- [ ] 동일/매칭 lens family
- [ ] 동일 FOV 및 focus distance
- [ ] exposure time 일치
- [ ] aperture/depth-of-field 일치
- [ ] illuminant SPD 기록
- [ ] film stock batch 기록
- [ ] processing chemistry 기록
- [ ] digital sensor temperature 기록

## Measurement

- [ ] MTF50/MTF20뿐 아니라 full MTF curve
- [ ] noise power spectrum
- [ ] grain PSD 및 temporal autocorrelation
- [ ] spectral sensitivity
- [ ] scene-referred dynamic range
- [ ] flare/PSF
- [ ] color difference under multiple SPDs

## Exhibition

- [ ] 좌석별 FOV/ppd
- [ ] display/projector luminance calibration
- [ ] black floor
- [ ] room stray light
- [ ] screen/direct-view uniformity
- [ ] audio cue 제거

## Human study

- [ ] 사전 power analysis
- [ ] preregistration
- [ ] double blind
- [ ] randomization
- [ ] trained/untrained strata
- [ ] discrimination과 preference 분리
- [ ] equivalence test

---

# 참고문헌

[1] Eastman Kodak Company. **KODAK VISION3 50D Color Negative Film 5203/7203 — Technical Information.** 2026.  
https://www.kodak.com/content/pdfs/motion/KODAK-VISION3-50D-5203-7203-technical-information.pdf

[2] Nasse, H. H. **How to Read MTF Curves.** Carl Zeiss Camera Lens Division.  
https://lenspire.zeiss.com/photo/app/uploads/2018/04/Article-MTF-2008-EN.pdf

[3] Blackmagic Design. **Blackmagic URSA Cine 17K 65 — Technical Specifications.** Accessed 2026-08-17.  
https://www.blackmagicdesign.com/kr/products/blackmagicursacine/techspecs

[4] ARRI. **ARRI announces the small and lightweight ALEXA 265 camera, revolutionizing 65 mm cinematography.** 2024-12-05.  
https://www.arri.com/en/company/press/press-releases-2024/arri-announces-the-small-and-lightweight-alexa-265-camera-revolutionizing-65-mm-cinematography

[5] Canon Inc. **Canon develops CMOS sensor with 410 megapixels, the largest number of pixels ever achieved in a 35 mm full-frame sensor.** 2025-01-22.  
https://global.canon/en/news/2025/20250122.html

[6] Lasergraphics. **Director — 8mm to 70mm Motion Picture Film Scanner.** Accessed 2026-08-17.  
https://lasergraphics.com/director.html

[7] Ashraf, M., Chapiro, A., & Mantiuk, R. K. **Resolution limit of the eye — how many pixels can we see?** *Nature Communications*, 16, 9086 (2025).  
https://doi.org/10.1038/s41467-025-64679-2

[8] Digital Cinema Initiatives, LLC. **Digital Cinema System Specification v1.5.0; High Dynamic Range D-Cinema Addendum v1.2.2; Direct View Display D-Cinema Addendum v1.2.** 2024–2026.  
https://www.dcimovies.com/dci-specification/

[9] Samsung Electronics. **Samsung Introduces 14-Meter Onyx Cinema LED Display at CinemaCon 2026.** 2026.  
https://news.samsung.com/global/samsung-introduces-14-meter-onyx-cinema-led-display-at-cinemacon-2026

[10] Digital Cinema Initiatives, LLC. **DCI Announcements — DCSS 1.5.0 and 2026 HDR revisions.** 2026.  
https://www.dcimovies.com/announcements/

[11] Reiss, J. D. **A Meta-Analysis of High Resolution Audio Perceptual Evaluation.** *Journal of the Audio Engineering Society*, 64(6), 364–379 (2016). DOI: 10.17743/jaes.2016.0015.  
https://aes2.org/publications/elibrary-page/?id=18296

[12] **Analysis of User Preferences for Film Grain Noise in Images and Video Sequences.** *Electronic Imaging*, Human Vision and Electronic Imaging, 2024. DOI: 10.2352/EI.2024.36.11.HVEI-230.  
https://library.imaging.org/ei/articles/36/11/HVEI-230

---

## 최종 한 문장

**15/70 IMAX의 역사적 우위는 ‘아날로그라서 무한하다’가 아니라 당시 가능한 어떤 디지털 시스템보다 큰 광학 정보 채널을 실용화했다는 데 있었고, 2026년에는 그 정보량 자체보다 필름의 전체 전달함수와 거대 상영 생태계를 얼마나 정밀하고 경제적으로 복제하느냐가 진짜 병목이다.**
