import sys
import importlib


def main():
    try:
        algorithms = sys.argv[1]
    except IndexError:
        print "please input sort algorithms(upper) name"
        return -1

    try:
        run_num = int(sys.argv[2])
        list_len = int(sys.argv[3])
    except (IndexError, ValueError):
        run_num = 5
        list_len = 12

    name = "sort.%s" % algorithms
    try:
        package = importlib.import_module(name)
    except ImportError:
        print "not found sort algorithms: %s" % algorithms
        return -2

    object_name = '%sSort' % algorithms.title()
    if not hasattr(package, object_name):
        print "not found algorithms class: %s" % object_name
        return -3

    instance = getattr(package, object_name)
    function = getattr(instance, 'main')
    function(run_num=run_num, list_len=list_len)

    return 0


if __name__ == "__main__":
    sys.exit(main())
