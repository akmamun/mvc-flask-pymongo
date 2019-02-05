
def depth(d):
    if isinstance(d, dict):
        for k, v in iter(dict.items(d)):
            if isinstance(v,dict):
                print(k,v.values())
                # if isinstance(v, dict):
                #     print(v, v.values())
                    # if isinstance(v, dict):
                    #     print(v,len(dict.keys(v)), v, dict.values(v))

            else:
                print(k,v)

    return  d.values()





d = {
    "key1": 1,
    "key2": {
        "key3": 1,
        "key4": {
            "key5": 4
        }
    }
}

print(depth(d))

