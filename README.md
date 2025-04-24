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

## 설치 문제 해결

### Fish 쉘 설정 오류 해결

UV 설치 시 다음과 같은 오류가 발생할 수 있습니다:
```bash
mkdir: /Users/username/.config/fish/conf.d: Permission denied
ERROR: command failed: mkdir -p /Users/username/.config/fish/conf.d
```

이 오류는 fish 쉘 설정 디렉토리에 대한 권한 문제입니다. 다음과 같은 방법으로 해결할 수 있습니다:

#### 방법 1: 수동으로 디렉토리 생성
```bash
# 디렉토리 생성
mkdir -p ~/.config/fish/conf.d

# 권한 설정
chmod 755 ~/.config/fish
chmod 755 ~/.config/fish/conf.d

# 다시 UV 설치
curl -LsSf https://astral.sh/uv/install.sh | sh
```

#### 방법 2: sudo 없이 설치
```bash
# sudo를 제거하고 설치
curl -LsSf https://astral.sh/uv/install.sh | sh
```

#### 방법 3: 수동 설치
```bash
# UV 바이너리 다운로드
curl -L https://github.com/astral-sh/uv/releases/download/v0.6.16/uv-aarch64-apple-darwin -o uv

# 실행 권한 부여
chmod +x uv

# 설치 디렉토리로 이동
mv uv ~/.local/bin/
```

### 설치 확인
```bash
# UV 버전 확인
uv --version

# fish 쉘 설정 확인
cat ~/.config/fish/conf.d/uv.fish
```

### 추가 문제 해결

1. **PATH 설정 문제**
   - `~/.local/bin`이 PATH에 포함되어 있는지 확인:
   ```bash
   echo $PATH
   ```
   - 포함되어 있지 않다면 `~/.bashrc` 또는 `~/.zshrc`에 추가:
   ```bash
   export PATH="$HOME/.local/bin:$PATH"
   ```

2. **권한 문제**
   - `~/.local/bin` 디렉토리의 권한 확인:
   ```bash
   ls -ld ~/.local/bin
   ```
   - 필요한 경우 권한 수정:
   ```bash
   chmod 755 ~/.local/bin
   ```

3. **캐시 문제**
   - 설치 캐시 삭제 후 재시도:
   ```bash
   rm -rf ~/.cache/uv
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

## 기본 사용법

### 1. 패키지 설치
```bash
uv pip install requests
```

### 2. 프로젝트 초기화

아래 명령은 uv를 특정 디렉토리에 초기화 하는 방법이다. 

```bash
uv init my-project
cd my-project
```

현재 디렉토리에서 uv를 초기화 한다면 다음과 같이 작성하자. 

```bash
uv init
```

#### UV 초기화 시 생성되는 파일들

UV 초기화 시 다음과 같은 파일들이 생성됩니다:

1. **`pyproject.toml`**
   - 프로젝트의 메타데이터와 설정을 저장하는 파일
   - 주요 내용:
     ```toml
     [project]
     name = "my-project"
     version = "0.1.0"
     description = ""
     authors = []
     dependencies = []
     requires-python = ">=3.8"

     [build-system]
     requires = ["hatchling"]
     build-backend = "hatchling.build"

     [tool.uv]
     # UV 관련 설정
     ```

2. **`.python-version`**
   - 프로젝트에서 사용할 Python 버전을 지정하는 파일
   - 내용 예시:
     ```
     3.11
     ```

3. **`requirements.txt`**
   - 프로젝트의 의존성 목록을 저장하는 파일
   - 초기에는 비어있음
   - `uv pip freeze` 명령으로 업데이트됨

4. **`requirements-dev.txt`**
   - 개발 환경에서만 필요한 의존성 목록을 저장하는 파일
   - 초기에는 비어있음
   - `uv pip freeze --dev` 명령으로 업데이트됨

5. **`.venv/` 디렉토리**
   - 가상환경이 생성되는 디렉토리
   - Python 인터프리터와 설치된 패키지들이 저장됨
   - 주요 하위 디렉토리:
     - `bin/` (Unix) 또는 `Scripts/` (Windows): 실행 파일들이 위치
     - `lib/`: 설치된 패키지들이 위치
     - `include/`: C 확장 모듈 헤더 파일들이 위치

6. **`uv.lock`**
   - 의존성의 정확한 버전을 잠그는 파일
   - `uv lock` 명령으로 생성/업데이트됨
   - 내용 예시:
     ```toml
     [package]
     requests = "2.31.0"
     numpy = "1.24.0"
     ```

#### 파일 관리 팁

1. **`.gitignore`에 추가할 항목**
   ```gitignore
   # UV 관련
   .venv/
   __pycache__/
   *.pyc
   .python-version
   uv.lock
   ```

2. **파일 업데이트 방법**
   ```bash
   # 의존성 추가 후 잠금 파일 업데이트
   uv add requests
   uv lock

   # requirements.txt 업데이트
   uv pip freeze > requirements.txt
   uv pip freeze --dev > requirements-dev.txt
   ```

3. **파일 복원 방법**
   ```bash
   # requirements.txt로부터 의존성 설치
   uv pip install -r requirements.txt
   uv pip install -r requirements-dev.txt

   # 잠금 파일로부터 정확한 버전 설치
   uv sync
   ```

### 3. 의존성 추가
```bash
uv add requests
```

#### `uv add` vs `uv pip install` 명령어 비교

UV는 패키지 설치를 위한 두 가지 주요 명령어를 제공합니다. 각 명령어의 특징과 차이점을 알아보겠습니다:

1. **`uv add` 명령어**
   - **프로젝트 의존성 관리에 최적화**
     - `pyproject.toml` 파일에 의존성을 자동으로 추가
     - 프로젝트의 의존성 목록을 체계적으로 관리
     - 개발 의존성과 일반 의존성을 명확히 구분
   - **사용 예시**:
     ```bash
     # 기본 의존성 추가
     uv add requests
     
     # 개발 의존성 추가
     uv add --dev pytest
     
     # 특정 버전 추가
     uv add requests==2.31.0
     
     # 로컬 패키지 추가
     uv add -e ./local-package
     ```
   - **주요 특징**:
     - 프로젝트 의존성 목록을 자동으로 업데이트
     - 의존성 버전을 명시적으로 관리
     - 개발 환경과 프로덕션 환경의 의존성을 구분
     - 로컬 패키지 개발에 최적화

2. **`uv pip install` 명령어**
   - **일반적인 패키지 설치에 최적화**
     - pip와 유사한 사용법 제공
     - 전역 또는 가상환경에 패키지 설치
     - 프로젝트 의존성 목록에 자동으로 추가되지 않음
   - **사용 예시**:
     ```bash
     # 기본 설치
     uv pip install requests
     
     # 특정 버전 설치
     uv pip install requests==2.31.0
     
     # requirements.txt로부터 설치
     uv pip install -r requirements.txt
     
     # 개발 모드 설치
     uv pip install -e ./local-package
     ```
   - **주요 특징**:
     - pip와 호환되는 명령어 구조
     - 즉시 패키지 설치 가능
     - 의존성 목록 관리 없이 빠른 설치
     - 임시 패키지 설치에 적합

3. **언제 어떤 명령어를 사용해야 할까?**
   - **`uv add` 사용이 권장되는 경우**:
     - 프로젝트의 의존성을 체계적으로 관리할 때
     - 개발 의존성과 프로덕션 의존성을 구분해야 할 때
     - 의존성 버전을 명시적으로 관리해야 할 때
     - 팀 프로젝트에서 의존성을 공유해야 할 때
   
   - **`uv pip install` 사용이 권장되는 경우**:
     - 일회성 패키지 설치가 필요할 때
     - 임시로 패키지를 테스트할 때
     - pip 명령어와의 호환성이 필요할 때
     - 의존성 목록 관리가 필요 없을 때

4. **실제 사용 예시**:
   ```bash
   # 프로젝트 초기 설정
   uv init my-project
   cd my-project
   
   # 프로젝트 의존성 추가 (uv add 사용)
   uv add requests  # 기본 의존성
   uv add --dev pytest  # 개발 의존성
   
   # 일회성 패키지 설치 (uv pip install 사용)
   uv pip install ipython  # 대화형 개발용
   uv pip install black  # 코드 포맷팅
   
   # 의존성 목록 업데이트
   uv lock  # 의존성 잠금
   uv pip freeze > requirements.txt  # requirements.txt 생성
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