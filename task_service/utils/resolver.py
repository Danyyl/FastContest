import time


def resolve(code: str, func_name: str, input_data: str, output_data: str, data_func=int) -> dict:
    inputs = list(map(data_func, input_data.split("\n")))
    outputs = list(map(data_func, output_data.split("\n")))
    exec(compile(code, "mulstring", "exec"))
    my_func = locals()[func_name]
    start = time.time()
    for input, output in zip(inputs, outputs):
        res = my_func(input)
        assert(res == output)
    return {"status": "Done", "detail": "All test passed", "time": time.time() - start}

