# day05 경보 판단

## 이상한 줄
- 줄 번호(여러 개면 모두):
2  03:12  192.0.2.7    → DB  3306   permit
3  03:13  192.0.2.7    → DB  3306   permit
- 이유:

## 고친 구성도
```
(여기에 ASCII 구성도)
INTERNET ──── FW ──┬── DMZ    ( WEB )
                   └── INSIDE ( DB )
INTERNET → DB  :3306   차단
```
