import re
import nexussdk

regex_param = r"(:\s*param\s*(\w+)\s*:)\s*(.*)"
regex_return = r":\s*return\s*:\s*(.*)"

blacklist = [
    "http_get",
    "http",
    "http_put",
    "http_delete",
    "http_post",
    "http_patch",
    "is_response_valid"
    "List",
    "Dict",
    "quote_plus",
    "deprecate_2",
    "copy_this_into_that",
    "HTTPError"
]


def digest_doc(raw_doc):
    if raw_doc is None:
        return "(no documentation provided)"

    lines = raw_doc.strip().splitlines()

    doc_lines = []

    for line in lines:
        striped_line = line.strip()

        # check if this line is for a param
        match_param = re.findall(regex_param, striped_line)

        # check if this matches a return info
        match_return = re.findall(regex_return, striped_line)

        if match_param:
            str = "- *argument* **" + match_param[0][1] + "**: " + match_param[0][2]
            doc_lines.append(str)
        elif match_return:
            str = "- *returned*: " + match_return[0]
            doc_lines.append(str)
        else:
            doc_lines.append(striped_line)

    return "\n".join(doc_lines)



for package in dir(nexussdk):
    if package.startswith("_"):
        continue

    if package in blacklist:
        continue

    # print("-------------------------------------------------")
    print("# " + package)

    all_functions = dir(getattr(nexussdk, package))

    for func in all_functions:
        if func in blacklist:
            continue

        if (func[0] == "_") or (func[-1] == "_"):
            continue

        func_obj = getattr(getattr(nexussdk, package), func)

        if not callable(func_obj):
            continue

        func_name = func_obj.__name__
        func_doc = digest_doc(func_obj.__doc__)

        print("## " + str(func_name))
        print(str(func_doc))
        print("\n")

        # print("\t## " + func_name)






# from docstring_parser import parse
