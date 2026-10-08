# 보안 경보 파이프라인

보안 경보를 LLM으로 분석하고 일일 보고서를 생성한 뒤 웹훅으로 알림을 전송하는 파이프라인입니다.

## 주요 기능
1. JSON 설정 및 보안 경보 불러오기
2. LLM을 이용한 경보 요약
3. 위험도순 정렬 (high → medium → low)
4. 총평 작성 및 Markdown 보고서 저장
5. 사람의 확인이 필요한 경보 집계
6. 웹훅 알림 전송

## 실행 방법

**필요 패키지**
```bash
pip install requests
```

**필요 파일**
- `config.json`: 모델, 승인 기준, 보고서 폴더, 웹훅 URL 설정
- `events_1008.json`: 보안 경보 데이터
- `.env`: `GEMINI_API_KEY` 설정

**실행**
```bash
python pipeline.py
```

## 실행 결과
- `daily_report_YYYYMMDD.md` 보고서 생성
- 승인 필요 경보 건수 출력
- 웹훅 알림 전송
