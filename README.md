# trains
Punctuality of Swedish trains

## Getting started
First time:
```
$ python -m venv venv
$ source venv/bin/activate
$ pip install pandas seaborn
```
Later:
```
$ source venv/bin/activate
$ python -i run.py
```

## Example TRAFA API call
```
curl "https://api.trafa.se/api/data?query=T0604|andeltag|ar:2022|tid:01|tillforlit" | python -m json.tool
```

# TODO

- [ ] Which was the KTH article mentioned by Sandro? Does it use TRAFA data?
- [X] How is STM computed? It's supposed to weigh in "regularitet" somehow, that is fraction of trains the weren't cancelled, I think.
  - --> *STM beskriver hur stor andel av de planerade tågen (planerade dagen innan avgång) som ankommit slutstation i tid. På så sätt sammanvägs tågens regularitet (andel av de planerade tågen som framförts) med tågens punktlighet (andel av de framförda tågen som ankommit i tid) till ett tillförlitlighetsmått*
- [ ] Kolla var jag kan publicera en app. Enklast på Google? 
- [ ] När jag vet var jag kan publicera den, skapa en app. Utgå från kod i `main.py`, men hämta data från api istället (glöm ej att cacha på nåt smart sätt).

