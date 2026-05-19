import http.client
import json

SERVER = "localhost:8081"


def get(path):
    conn = http.client.HTTPConnection(SERVER)
    conn.request("GET", path)
    r1 = conn.getresponse()
    data = r1.read().decode()
    conn.close()
    return json.loads(data)


print(get("/listSpecies?json=1&limit=5"))
print(get("/karyotype?json=1&species=human"))
print(get("/chromosomeLength?json=1&species=human&chromo=1"))
print(get("/geneLookup?json=1&gene=FRAT1"))
print(get("/geneSeq?json=1&gene=FRAT1"))
print(get("/geneInfo?json=1&gene=FRAT1"))
print(get("/geneCalc?json=1&gene=FRAT1"))
print(get("/geneList?json=1&chromo=1&start=100000&end=200000"))