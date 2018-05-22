import shutil
import os
import sys
def test001():
    print("this is a simple test")



def replace_in_text(txt = '''
    this is the first_line
    this is going to be replaced
    there is a pattern001 which is going to be replaced in this line
    this is the last_line   
    '''
    , replacements = {
        "replaced": "replacement"
        , "pattern001": "right_one"
    }
):
    for line in txt.split("\n"):
        for src, target in replacements.items():
            # notice, if you did: src, target = replacements.items... then: src = ('replaced', 'replacement')
            # # there will be a bunch of comments... to remove them
            # # # sed -e "/^\s*#/d" this_file.py > file_without_comments
            line = line.replace(src, target)
        print(line)
    pass

def replace_in_file(
        path_file_input = "ti.txt",
        path_file_output = "ta.txt",
        replacements = {
            "coco": 'toto',
            "tic": """tac
            this is going to be a very long txt
            hereis not yet the end
            looks like this is the end
            finally, the end"""
        }
):
    with open(path_file_input) as infile, open(path_file_output, 'w') as outfile:
        for line in infile:
            for src, target in replacements.items():
                line = line.replace(src, target)
            outfile.write(line)
    pass

def print_var_type_n_val(
    var001 = "A"
    , pointer = "#eto001"
):
    if (
        ( '-m' not in sys.argv[0])
    ):
        path_file = os.path.abspath(os.path.dirname(sys.argv[0])) + '\\' + sys.argv[0]
    else:
        path_file = os.path.abspath(os.path.dirname(sys.argv[1])) + '\\' + sys.argv[1]

    # print("sys.argv[0]: ", "-m" in sys.argv[0])
    # # print(sys.argv[1])
    # print("path_file: ", path_file)

    if(len(str(var001).split()) == 1):
        replace_in_file( #OK
            path_file_input = path_file
            , path_file_output = path_file + "_tmp"
            , replacements = {
                pointer + '_': pointer + "\n# Value: " + str(var001) + "\n# Type: " + str(type(var001))
            }
        )
        shutil.move(path_file + "_tmp", path_file)
    else:
        # commented_long_text = '#' + '#'.join(
        #     map(str, var001.split())
        # ) + "\n"

        commented_long_text = ''
        for s in map(str, str(var001).split('\n')):
            commented_long_text += '# # ' + s + '\n'
            pass
        replace_in_file( #OK
            path_file_input = path_file
            , path_file_output = path_file + "_tmp"
            , replacements = {
                pointer + '_': pointer + "\n# Value: \n" + str(commented_long_text) + "\n# Type: " + str(type(var001))
            }
        )
        shutil.move(path_file + "_tmp", path_file)
        pass
    pass


def copy_file(
    src_file = "e:\\src_file.txt"
    , target_file = "e:\\target_file.txt"
):
    with open(src_file, 'rb') as read_src, open(target_file, 'wb') as write_target:
        for line in read_src:
            write_target.write(line)
    pass
