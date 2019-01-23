import re
import nexussdk

regex_param = r"(:\s*param\s*(\w+)\s*:)\s*(.*)"
regex_return = r":\s*return\s*:\s*(.*)"

toc = ""
doc = ""


blacklist = [
    "http_get",
    "http",
    "http_put",
    "http_delete",
    "http_post",
    "http_patch",
    "is_response_valid",
    "List",
    "Dict",
    "quote_plus",
    "url_encode",
    "deprecate_2",
    "copy_this_into_that",
    "HTTPError",
    "utils"
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




def add_to_doc(line):
    global doc
    doc = doc + line + "\n"

def add_to_toc(entry, level):
    global toc
    whitelist = set('abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ_')
    link = ''.join(filter(whitelist.__contains__, entry))
    link = "#" + re.sub("\s+", "-", link)

    toc = toc + ("\t" * level) + "- [" + entry + "](" + link + ")\n"



for package in dir(nexussdk):
    if package.startswith("_"):
        continue

    if package in blacklist:
        continue

    package_obj = getattr(nexussdk, package)

    add_to_toc(package, 0)
    add_to_doc("# " + package)

    package_doc = digest_doc(package_obj.__doc__)
    add_to_doc(package_doc)

    # print(package)

    all_functions = dir(package_obj)

    for func in all_functions:

        if func in blacklist:
            continue

        if (func[0] == "_") or (func[-1] == "_"):
            continue

        func_obj = getattr(package_obj, func)

        if not callable(func_obj):
            continue

        func_name = str(func_obj.__name__)

        if func_name in blacklist:
            continue

        # print("\t" + func_name)

        func_doc = digest_doc(func_obj.__doc__)

        subtitle = package + ": " + str(func_name)

        add_to_doc("## " + subtitle)
        add_to_toc(subtitle, 1)

        add_to_doc(str(func_doc))
        add_to_doc("\n")

print("Documentation of Nexus Python SDK")
print("# Table of content")
print(toc)
print('')
print(doc)
