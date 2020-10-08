from subprocess import PIPE, Popen, check_output, run


def execute(arr):
    process = None

    if len(arr) == 1:
        return run(arr[0], stdout=PIPE).stdout.decode('utf-8').rstrip()
    for index, command in enumerate(arr):
        if(index < len(arr) - 1):
            p1 = None
            if(process != None):
                p1 = Popen(command, stdout=PIPE, stdin=process.stdout)
            else:
                p1 = Popen(command, stdout=PIPE)

            p2 = Popen(arr[index + 1], stdin=p1.stdout, stdout=PIPE)
            p1.stdout.close()
            process = p2
        else:
            value = process.stdout.read().decode('utf-8').rstrip()
            process.stdout.close()
            return value
