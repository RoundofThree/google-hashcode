import subprocess

def solve(inp, args):
    # hardcode here your cpp filename 
    filename = "test.cpp"
    executable = "test"
    compile_message = subprocess.getoutput('g++ cpp_solvers/' + filename + ' -o ' + executable)
    
    if compile_message == "":
        process = subprocess.Popen(["./" + executable], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        ret, err = process.communicate()
        print(ret)
        return ret.decode('utf-8')
    else:
        print(compile_message) # not compiled or any warnings 
