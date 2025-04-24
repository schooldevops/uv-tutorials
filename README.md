# UV 튜토리얼

UV는 Rust로 작성된 매우 빠른 Python 패키지 및 프로젝트 관리자입니다. 이 튜토리얼에서는 UV의 설치부터 기본적인 사용법까지 단계별로 알아보겠습니다.

## 목차
1. [UV 소개](#uv-소개)
2. [설치 방법](#설치-방법)
3. [기본 사용법](#기본-사용법)
4. [UV vs pip 비교](#uv-vs-pip-비교)
5. [실습 튜토리얼](#실습-튜토리얼)

## UV 소개

UV는 Python 패키지 관리와 프로젝트 관리를 위한 현대적인 도구입니다. 주요 특징은 다음과 같습니다:

- ⚡️ pip보다 10-100배 빠른 속도
- 🐍 Python 버전 관리 지원
- 🗂️ 종합적인 프로젝트 관리 기능
- 💾 디스크 공간 효율적인 전역 캐시
- 🖥️ macOS, Linux, Windows 지원

## 설치 방법

### macOS 및 Linux
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Windows
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### pip를 통한 설치
```bash
pip install uv
```

## 기본 사용법

### 1. 패키지 설치
```bash
uv pip install requests
```

### 2. 프로젝트 초기화
```bash
uv init my-project
cd my-project
```

### 3. 의존성 추가
```bash
uv add requests
```

### 4. 가상환경 생성
```bash
uv venv
```

### 5. 스크립트 실행
```bash
uv run script.py
```

## UV vs pip 비교

### 속도
- UV: 매우 빠름 (10-100배)
- pip: 상대적으로 느림

### UV의 성능 최적화 원리

UV가 pip보다 빠른 이유는 다음과 같은 기술적 최적화 때문입니다:

1. **Rust 구현**
   - UV는 Python이 아닌 Rust로 작성되어 있습니다.
   - Rust는 컴파일 언어로, Python보다 더 빠른 실행 속도를 제공합니다.
   - 메모리 안전성과 동시성 처리가 우수합니다.

2. **병렬 처리 최적화**
   - 패키지 의존성 해결과 설치를 병렬로 처리합니다.
   - 다중 스레드를 활용하여 여러 패키지를 동시에 처리합니다.
   - pip는 기본적으로 순차적으로 패키지를 처리합니다.

3. **전역 캐시 시스템**
   - 다운로드한 패키지를 전역적으로 캐싱합니다.
   - 동일한 패키지를 여러 프로젝트에서 재사용할 수 있습니다.
   - pip는 프로젝트별로 패키지를 다시 다운로드합니다.

4. **의존성 해결 알고리즘**
   - PubGrub 알고리즘을 사용하여 의존성 해결을 최적화합니다.
   - 충돌하는 의존성을 더 효율적으로 해결합니다.
   - pip는 단순한 의존성 해결 전략을 사용합니다.

5. **디스크 I/O 최적화**
   - 패키지 설치 시 디스크 쓰기 작업을 최소화합니다.
   - 하드 링크를 사용하여 디스크 공간을 효율적으로 관리합니다.
   - pip는 매번 새로운 파일을 생성합니다.

6. **네트워크 최적화**
   - 패키지 다운로드 시 연결 풀링을 사용합니다.
   - HTTP/2를 지원하여 더 효율적인 네트워크 통신을 제공합니다.
   - pip는 기본 HTTP/1.1을 사용합니다.

7. **메모리 관리**
   - Rust의 소유권 시스템을 활용하여 효율적인 메모리 관리를 합니다.
   - 불필요한 메모리 할당과 복사를 최소화합니다.
   - pip는 Python의 가비지 컬렉션에 의존합니다.

8. **의존성 트리 최적화**
   - 의존성 트리를 더 효율적으로 구성합니다.
   - 중복된 패키지 설치를 최소화합니다.
   - pip는 의존성 트리를 최적화하지 않습니다.

### 기능
- UV:
  - 통합된 프로젝트 관리
  - Python 버전 관리
  - 전역 캐시 시스템
  - 스크립트 실행 지원
- pip:
  - 기본적인 패키지 관리
  - 제한된 기능

### 사용성
- UV:
  - 현대적인 CLI 인터페이스
  - 직관적인 명령어
  - 자동화된 환경 관리
- pip:
  - 전통적인 인터페이스
  - 수동 환경 관리 필요

## 실습 튜토리얼

### 1. 프로젝트 생성 및 설정
```bash
# 새 프로젝트 생성
uv init my-first-project
cd my-first-project

# 가상환경 생성
uv venv

# 활성화 (macOS/Linux)
source .venv/bin/activate
# Windows
.venv\Scripts\activate
```

### 2. 패키지 설치 실습
```bash
# requests 패키지 설치
uv pip install requests

# 여러 패키지 한 번에 설치
uv pip install requests pandas numpy
```

### 3. 프로젝트 의존성 관리
```bash
# requirements.txt 생성
uv pip freeze > requirements.txt

# requirements.txt로부터 설치
uv pip install -r requirements.txt
```

### 4. Python 버전 관리
```bash
# Python 3.11 설치
uv python install 3.11

# 특정 Python 버전 사용
uv run --python 3.11 script.py
```

### 5. 스크립트 실행
```python
# test.py 파일 생성
import requests
response = requests.get('https://api.github.com')
print(response.status_code)
```

```bash
# 스크립트 실행
uv run test.py
```

## UV 명령어 사용법

UV는 다양한 명령어를 제공합니다. 각 명령어의 상세한 사용법과 옵션을 알아보겠습니다:

### 1. 패키지 관리 명령어
```bash
# 기본 패키지 설치
uv pip install requests  # requests 패키지 설치

# 특정 버전 설치
uv pip install requests==2.31.0  # requests 2.31.0 버전 설치
uv pip install "requests>=2.31.0"  # requests 2.31.0 이상 버전 설치
uv pip install "requests<3.0.0"  # requests 3.0.0 미만 버전 설치

# 개발 의존성 설치
uv pip install --dev pytest  # 개발 환경에서만 필요한 패키지 설치
uv pip install --dev black isort mypy  # 여러 개발 도구 한 번에 설치

# 패키지 제거
uv pip uninstall requests  # requests 패키지 제거
uv pip uninstall -y requests  # 확인 없이 바로 제거

# 패키지 업그레이드
uv pip install --upgrade requests  # requests 패키지 최신 버전으로 업그레이드
uv pip install --upgrade pip  # pip 자체 업그레이드

# 패키지 검색
uv pip search "data science"  # 키워드로 패키지 검색

# 패키지 정보 확인
uv pip show requests  # requests 패키지 상세 정보 확인
uv pip list  # 설치된 모든 패키지 목록 확인
uv pip list --outdated  # 업그레이드가 필요한 패키지 목록 확인
```

### 2. 프로젝트 관리 명령어
```bash
# 새 프로젝트 생성
uv init my-project  # 기본 프로젝트 생성
uv init my-project --python 3.11  # 특정 Python 버전으로 프로젝트 생성
uv init my-project --no-venv  # 가상환경 없이 프로젝트 생성

# 의존성 관리
uv add requests  # requests 패키지 추가
uv add requests==2.31.0  # 특정 버전의 requests 추가
uv add --dev pytest  # 개발 의존성으로 pytest 추가
uv add -e ./local-package  # 로컬 패키지를 개발 모드로 추가

# 의존성 제거
uv remove requests  # requests 패키지 제거
uv remove --dev pytest  # 개발 의존성 제거

# 의존성 동기화
uv sync  # 모든 의존성 설치/업데이트
uv sync --dev  # 개발 의존성 포함하여 동기화
uv sync --no-dev  # 개발 의존성 제외하고 동기화

# 의존성 잠금
uv lock  # 현재 의존성 상태를 잠금 파일에 저장
uv lock --dev  # 개발 의존성 포함하여 잠금
uv lock --no-dev  # 개발 의존성 제외하고 잠금
```

### 3. 가상환경 명령어
```bash
# 가상환경 생성
uv venv  # 기본 가상환경 생성
uv venv --python 3.11  # Python 3.11로 가상환경 생성
uv venv --name myenv  # 특정 이름으로 가상환경 생성
uv venv --clear  # 기존 가상환경 삭제 후 새로 생성

# 가상환경 활성화
# macOS/Linux
source .venv/bin/activate  # 기본 가상환경 활성화
source myenv/bin/activate  # 특정 이름의 가상환경 활성화

# Windows
.venv\Scripts\activate  # 기본 가상환경 활성화
myenv\Scripts\activate  # 특정 이름의 가상환경 활성화

# 가상환경 비활성화
deactivate  # 모든 운영체제에서 동일
```

### 4. Python 버전 관리 명령어
```bash
# Python 설치
uv python install 3.11  # Python 3.11 설치
uv python install 3.11.0  # 특정 마이너 버전 설치
uv python install 3.11 --force  # 강제로 재설치

# Python 버전 관리
uv python list  # 설치된 Python 버전 목록
uv python remove 3.11  # Python 3.11 제거
uv python pin 3.11  # 현재 디렉토리의 Python 버전을 3.11로 고정

# 특정 Python 버전 사용
uv run --python 3.11 script.py  # Python 3.11로 스크립트 실행
uv run --python 3.11 -m pytest  # Python 3.11로 pytest 실행
```

### 5. 스크립트 실행 명령어
```bash
# 기본 스크립트 실행
uv run script.py  # script.py 실행
uv run -m module  # Python 모듈 실행

# 의존성과 함께 실행
uv run --with-deps script.py  # 필요한 의존성 설치 후 스크립트 실행
uv run --no-deps script.py  # 의존성 설치 없이 스크립트 실행

# 인자 전달
uv run script.py --arg1 value1 --arg2 value2  # 스크립트에 인자 전달
uv run -m pytest tests/ --verbose  # pytest에 옵션 전달

# 환경 변수 설정
uv run --env VAR1=value1 --env VAR2=value2 script.py  # 환경 변수 설정
```

## 실전 활용 예제

### 1. 데이터 과학 프로젝트 설정
```bash
# 프로젝트 생성 및 설정
uv init data-science-project --python 3.11
cd data-science-project

# 데이터 분석 필수 패키지 설치
uv pip install pandas==2.1.0 numpy==1.24.0 matplotlib==3.7.0
uv pip install scikit-learn==1.3.0 seaborn==0.12.0

# Jupyter 환경 설정
uv pip install --dev jupyter==1.0.0 notebook==7.0.0
uv pip install --dev ipykernel==6.25.0

# 코드 품질 도구 설치
uv pip install --dev black==23.7.0 isort==5.12.0 flake8==6.1.0
uv pip install --dev mypy==1.5.0 pytest==7.4.0

# 의존성 관리
uv lock  # 현재 상태를 잠금 파일에 저장
uv pip freeze > requirements.txt  # requirements.txt 생성
uv pip freeze --dev > requirements-dev.txt  # 개발 의존성만 따로 저장

# Jupyter 커널 등록
uv run python -m ipykernel install --user --name=data-science --display-name="Python (Data Science)"
```

### 2. 웹 개발 프로젝트 설정 (FastAPI)
```bash
# 프로젝트 생성
uv init web-api --python 3.11
cd web-api

# FastAPI 및 관련 패키지 설치
uv pip install fastapi==0.103.0 uvicorn==0.23.0
uv pip install sqlalchemy==2.0.20 alembic==1.12.0
uv pip install pydantic==2.3.0 python-jose==3.3.0 passlib==1.7.4

# 개발 도구 설치
uv pip install --dev pytest==7.4.0 httpx==0.24.1
uv pip install --dev black==23.7.0 isort==5.12.0
uv pip install --dev mypy==1.5.0 types-requests==2.31.0.2

# 데이터베이스 마이그레이션 설정
uv run alembic init migrations
uv run alembic revision --autogenerate -m "initial migration"
uv run alembic upgrade head

# 개발 서버 실행
uv run uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### 3. 기계 학습 프로젝트 설정 (PyTorch)
```bash
# 프로젝트 생성
uv init ml-project --python 3.11
cd ml-project

# PyTorch 설치 (CUDA 지원)
uv pip install torch==2.0.1 torchvision==0.15.2 torchaudio==2.0.2 \
    --index-url https://download.pytorch.org/whl/cu118

# 추가 ML 라이브러리 설치
uv pip install transformers==4.31.0 datasets==2.14.0
uv pip install wandb==0.15.4 tensorboard==2.13.0
uv pip install scikit-learn==1.3.0 optuna==3.2.0

# 개발 도구 설치
uv pip install --dev jupyter==1.0.0 black==23.7.0
uv pip install --dev pytest==7.4.0 pytest-cov==4.1.0

# 실험 관리 설정
uv run wandb login  # Weights & Biases 로그인
uv run tensorboard --logdir=./logs  # TensorBoard 실행
```

### 4. CI/CD 파이프라인 설정
```bash
# 의존성 설치 및 캐싱
uv pip install -r requirements.txt
uv pip install -r requirements-dev.txt

# 코드 품질 검사
uv run black . --check  # 코드 포맷팅 검사
uv run isort . --check-only  # import 정렬 검사
uv run flake8 .  # 린트 검사
uv run mypy .  # 타입 체크

# 테스트 실행
uv run pytest tests/ --cov=src --cov-report=xml  # 테스트 및 커버리지
uv run pytest tests/ --junitxml=test-results.xml  # JUnit 형식 결과

# 문서 생성
uv pip install --dev sphinx==7.1.2 sphinx-rtd-theme==1.3.0
uv run sphinx-build -b html docs/ docs/_build/html
```

### 5. 멀티 버전 Python 프로젝트
```bash
# 여러 Python 버전 설치
uv python install 3.9 3.10 3.11

# 각 버전별 테스트 실행
for version in 3.9 3.10 3.11; do
    uv run --python $version pytest tests/ --junitxml=test-results-$version.xml
done

# 버전별 의존성 설치
uv run --python 3.9 pip install -r requirements-py39.txt
uv run --python 3.10 pip install -r requirements-py310.txt
uv run --python 3.11 pip install -r requirements-py311.txt

# 버전별 코드 품질 검사
for version in 3.9 3.10 3.11; do
    uv run --python $version black . --check
    uv run --python $version isort . --check-only
    uv run --python $version mypy .
done
```

## 결론

UV는 Python 개발 환경을 더 빠르고 효율적으로 만들어주는 강력한 도구입니다. pip와 비교하여 더 나은 성능과 기능을 제공하며, 특히 대규모 프로젝트나 빠른 개발이 필요한 상황에서 유용합니다.

이 튜토리얼을 통해 UV의 기본적인 사용법을 익혔습니다. 더 자세한 내용은 [공식 문서](https://docs.astral.sh/uv/)를 참고하세요. 