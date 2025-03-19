from submission_template.model import Model


def eval():
    model = Model()
    result = model.evaluate()
    with open("/tmp/output.txt", "w") as f:
        f.write(str(result))


if __name__ == "__main__":
    eval()
