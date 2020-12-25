def auto(case, one, two, tag="equal"):
    # 通用断言
    # case:TestCase类本身,one:比较第一个值,two:比较第二个值
    # equal:(使用等于断言) more(第一个值 大于 第二个值) in(第一个值 在 第二个值里)
    if tag == "equal":
        case.assertEqual(one, two)

    if tag == "more":
        case.assertTrue(one > two)

    if tag == "in":
        case.assertTrue(one in two)