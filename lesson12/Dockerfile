FROM python:3-slim
WORKDIR /math
COPY math/test_math.py /math
COPY math/math_lib.py /math
CMD ["python", "-m", "unittest"]