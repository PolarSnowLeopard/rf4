# 使用Python 3.12作为基础镜像
FROM python:3.12-slim

# 设置工作目录
WORKDIR /app

# 设置环境变量
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# 安装uv
RUN pip install --no-cache-dir uv

# 复制项目文件
COPY pyproject.toml uv.lock ./
COPY app/ ./

# 使用uv安装依赖
RUN uv pip install --system -e .

# 暴露端口
EXPOSE 9999

# 启动命令
CMD ["python", "-m", "gunicorn", "rf4.asgi:application", "-k", "uvicorn.workers.UvicornWorker", "-b", "0.0.0.0:9999"]