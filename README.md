# staff-learning-assistant

## Environment

Python 3.8+

## Python Guide

[from import](https://juejin.cn/post/7087069728371376164)

## Dependencies

please read requirements.txt

## Install

install dependencies

    pip3 install -r requirements.txt

## Store dependencies

    pipreqs . --encoding=utf8 --force

if you did not install pipreqs please run this:

    pip3 install pipreqs -i https://pypi.python.org/simple/ 

## API KEY
### Set this to `azure`
    export OPENAI_API_TYPE=azure
### The API version you want to use: set this to `2023-03-15-preview` for the released version.
    export OPENAI_API_VERSION=2023-03-15-preview
### The base URL for your Azure OpenAI resource.  You can find this in the Azure portal under your Azure OpenAI resource.
    export OPENAI_API_BASE=https://your-resource-name.openai.azure.com
### The API key for your Azure OpenAI resource.  You can find this in the Azure portal under your Azure OpenAI resource.
    export OPENAI_API_KEY=<your Azure OpenAI API key>

## LangChain

[中文教程](https://www.jianshu.com/p/f26c7191944d)

### Chain

[Chain中文教程(javascript)](https://zhuanlan.zhihu.com/p/634313377)


### Token

Tools:

[tokenizer](https://platform.openai.com/tokenizer)

Limit:

[model token limit](https://platform.openai.com/docs/models/overview)

    gpt-3.5-turbo	    4,096 tokens
    gpt-3.5-turbo-16k	16,384 tokens

Pricing:

[token pricing](https://openai.com/pricing)

    Model               Input                   Output
    gpt-3.5-turbo	    $0.0015 / 1K tokens     $0.002 / 1K tokens
    gpt-3.5-turbo-16k	$0.003 / 1K tokens      $0.004 / 1K tokens

## Open AI

## Restful API

### FastAPI

[FastAPI](https://fastapi.tiangolo.com/zh/tutorial/)

[FastAPI QuickStart](https://zhuanlan.zhihu.com/p/624779536)

[uvicorn](https://zhuanlan.zhihu.com/p/115237857)

Upload Files:

[FastApi upload multiple file](https://fastapi.tiangolo.com/tutorial/request-files/#multiple-file-uploads)
[FastApi File path](https://self-methods.com/fastapi-file/)

#### Swagger UI

    http://127.0.0.1:5000/docs

#### ReDoc UI

    http://127.0.0.1:5000/redoc

#### OpenAPI Url

    http://127.0.0.1:5000/openapi.json

### pydantic model

[pydantic](https://juejin.cn/post/7079027549896081421)

### Unstructured

[Unstructured解析文件](https://unstructured-io.github.io/unstructured/installing.html)

[Langchain + Unstructured](https://python.langchain.com/docs/modules/data_connection/document_loaders/integrations/unstructured_file)

#### libreoffice

Unstructured 解析word, excel, ppt需要那使用libreoffice

[Mac OS X](https://formulae.brew.sh/cask/libreoffice)


# Vector Database

[Milvus VS FAISS](https://www.libhunt.com/compare-milvus-vs-faiss)

## Milvus

[Milvus](https://milvus.io/docs/install_standalone-docker.md)

[Langchain + Milvus](https://python.langchain.com/docs/modules/data_connection/vectorstores/integrations/milvus)

[中文教程](https://zhuanlan.zhihu.com/p/405186060)

[中文教程](http://www.yishuifengxiao.com/2022/12/27/%E5%90%91%E9%87%8F%E6%90%9C%E7%B4%A2%E6%95%B0%E6%8D%AE%E5%BA%93milvus%E5%85%A5%E9%97%A8%E6%95%99%E7%A8%8B/)

[术语](https://blog.csdn.net/leaning_java/article/details/130344223)

## FAISS

[FAISS](https://faiss.ai/)

[Langchain + FAISS](https://python.langchain.com/docs/modules/data_connection/vectorstores/integrations/faiss)

[Langchain + FAISS](https://ict-worker.com/ai/gpt35-with-smeca.html)

[FAISS + llama.cpp](https://hackernoon.com/a-practical-5-step-guide-to-do-semantic-search-on-your-private-data-with-the-help-of-llms)

[FAISS 集群解说](https://zhuanlan.zhihu.com/p/320653340)

[FAISS 集群](https://github.com/facebookresearch/faiss/blob/main/demos/demo_client_server_ivf.py)

[FAISS Langchain 相似度兼容](https://blog.csdn.net/weixin_43913406/article/details/131215407)

[FAISS remove index](https://github.com/facebookresearch/faiss/wiki/Special-operations-on-indexes#removing-elements-from-an-index)

## AI FLow UML

[FlowiseAi](https://flowiseai.com/?ref=hackernoon.com)

# Error Fix

## unable to get local issuer certificate

    [nltk_data] Error loading punkt: <urlopen error [SSL:
    [nltk_data]     CERTIFICATE_VERIFY_FAILED] certificate verify failed:
    [nltk_data]     unable to get local issuer certificate (_ssl.c:1129)>
    [nltk_data] Error loading averaged_perceptron_tagger: <urlopen error
    [nltk_data]     [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify
    [nltk_data]     failed: unable to get local issuer certificate
    [nltk_data]     (_ssl.c:1129)>

Fix:
    
    https://stackoverflow.com/questions/52805115/certificate-verify-failed-unable-to-get-local-issuer-certificate

    Environment: Mac, Python 3.10, iTerm,

    Search in Finder: Install Certificates.command

    enter image description here

    Get Info enter image description here

    Open with: iTerm.app

    enter image description here

    double click 'Install Certificates.command'

    Waiting for install the certificates. Solve it.

## this version of sdk is incompatible with server, please downgrade your sdk or upgrade your server

this version of sdk is incompatible with server, please downgrade your sdk or upgrade your server

FIX:

    https://github.com/milvus-io/milvus/discussions/24913
    https://softhints.com/installing-specific-package-versions-with-pip/

Step:

    1. uninstall pymilvus
        pip3 uninstall pymilvus
    2. install old version
        pip3 install pymilvus==<version>
        pip3 install pymilvus==2.2.3
    3. check version
        pip3 show pymilvus

## openai.error.InvalidRequestError: Too many inputs. The max number of inputs is 1.  We hope to increase the number of inputs per request soon.

    openai.error.InvalidRequestError: Too many inputs. The max number of inputs is 1.  We hope to increase the number of inputs per request soon.

Fix:

    https://github.com/hwchase17/langchain/issues/4575

Step:
    
    # option 1
    # change chunk_size to 1
    text_splitter = CharacterTextSplitter.from_tiktoken_encoder(
        chunk_size=1, chunk_overlap=0
    )
    docs = text_splitter.split_documents(documents)
    # but it will generate too much Documents

    # option 2
    
## Could not automatically map staff-learning-assistant-model-01 to a tokeniser. Please use `tiktok.get_encoding` to explicitly get the tokeniser you expect.

    Could not automatically map staff-learning-assistant-model-01 to a tokeniser. Please use `tiktok.get_encoding` to explicitly get the tokeniser you expect.

Fix:

    https://github.com/openai/tiktoken/pull/72
    https://github.com/openai/tiktoken/issues/73

    version fix: 
    

Step:

    # change "gpt-35-turbo" to "gpt-3.5-turbo" when you init AzureOpenAI
    AzureOpenAI(
        engine="staff-learning-assistant-model-01",
        model_name="gpt-3.5-turbo"
    )

## FileNotFoundError: soffice command was not found. Please install libreoffice

    FileNotFoundError: soffice command was not found. Please install libreoffice

Fix:
    
    需要安装libreoffice, 它是解析Micosoft的办公套件的工具

    - Install instructions: https://www.libreoffice.org/get-help/install-howto/
    - Mac: https://formulae.brew.sh/cask/libreoffice
    - Debian: https://wiki.debian.org/LibreOffice

Step:

    Mac:
    brew update
    brew install --cask libreoffice