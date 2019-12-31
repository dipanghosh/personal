import pandas as pd

logfilepath = "pred-sweep-2006-2007.log"


def filter_garbage(e):
    if e in ["", "\n", "[", "]", " "]:
        return False
    else:
        return True


def retrieve_pred_from_log(logfilepath):

    pred_from_log = {}
    logfile = open(logfilepath, "r")
    for line in logfile.readlines():
        if line.rstrip():
            line = "".join((filter(filter_garbage, line)))
            date = int(line.split(",")[0])
            pred = line.split(",")[1:]
            if pred[0] == "":
                pred_from_log[date] = []
            else:
                pred = list(map(float, pred))
                pred_from_log[date] = pred
    return pred_from_log


if __name__ == "__main__":

    df = pd.DataFrame.from_dict(retrieve_pred_from_log(logfilepath), orient='index')
    df.to_csv(logfilepath.split("-")[-1].replace(".log", ".csv"))
