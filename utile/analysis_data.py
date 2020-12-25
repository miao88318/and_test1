import json, os


class AnalysisData:
    @classmethod
    def get_json_data(cls, file, fk="", sk=[]):

        fk_list = []
        with open("./data" + os.sep + file, "r", encoding="utf-8")as f:
        # with open(r"C:\python\and_test1\data" + os.sep + file, "r", encoding="utf-8")as f:
            json_data = json.load(f)
            if fk:
                value = json_data.get(fk)
                if sk:
                    for i in value:
                        sk_value = []
                        for x in sk:
                            sk_value.append(i.get(x))
                        fk_list.append(tuple(sk_value))
                    return fk_list

# if __name__ == '__main__':
#     x = AnalysisData.get_json_data("home.json", "banner", ["banner_code", "banner_id", "banner_name", "banner_length"])
#     print(x)
