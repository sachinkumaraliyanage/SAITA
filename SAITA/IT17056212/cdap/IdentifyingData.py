from Query import Queries
from Inputs import Input
from difflib import SequenceMatcher


def get_netarr():
    inp = Input.get_input()
    if inp.get_component() == 'identifying':
        if inp.get_category() == 'network':
            # print("ident cat" + inp.get_component())
            # print("ident cat" + inp.get_category())
            net_arr = []

            result = Queries.get_all_networkerrors()
            # print(result)
            for x in result:

                # compare similarity ratio
                errormsg = x[0]
                ratio = SequenceMatcher(None, errormsg, inp.get_error_msg()).ratio()
                if ratio > 0.9:
                    x = list(x)
                    x[0] = inp.get_error_msg()
                    x = tuple(x)
                    print('Changed after similarity check: '+x[0])
                else:
                    x = list(x)
                    x[0] = errormsg
                    x = tuple(x)

                pre_split_field = x[1] + "/" + "none"
                split_field = pre_split_field.split("/")
                # print(len(split_field))
                for y in split_field:
                    a = [x[0], y, x[2], x[3]]

                    net_arr.append(a)

            print(net_arr)
            return net_arr
