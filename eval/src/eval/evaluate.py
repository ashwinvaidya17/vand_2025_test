import json

from submission_template.model import Model


def eval():
    model = Model()
    result = model.evaluate()
    with open("results.json", "w") as f:
        json.dump(result, f)


if __name__ == "__main__":
    eval()
