from selenium_wrapper import SeleniumWrapper


if __name__ == '__main__':

    url = "https://www.ebay.com/sch/FindingCustomization/?_fcsp=https%3A//www.ebay.com/sch/i.html%3F_from%3DR40%26_sacat%3D0%26_nkw%3D%26_pppn%3Dr1%26scp%3Dce0&_fcsbm=1&_pppn=v3&_fcdm=1&_fcss=12&_fcps=3&_fcippl=1&_fcso=1&_fcpd=1&_fcpe=3%7C2%7C4&_fcie&_fcse=42%7C43%7C10"
    params_searcher = {
        "element_name": "gh-ac",
        "expected_condition": "visibility_of_element_located",
        "search_By": "ID"
    }
    example = SeleniumWrapper()
    example.visit(url)
    print(example.get_element(**params_searcher))