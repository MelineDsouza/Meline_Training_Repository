dictionry = {
  "brand": "Ford",
  "model": "honda",
  "year": 1964
}
print(dictionry)

print(len(dictionry))
x = dictionry.values()
print(x)


dictionry.update({"year": 2020})
print(dictionry)

dictionry["color"] = "red"
print(dictionry)


dictionry.pop("model")
print(dictionry)

dictionry["model"] = "mustang"
print(dictionry)