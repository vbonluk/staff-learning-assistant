from pydantic import BaseModel
from typing import List


class URLScrapeRequestBody(BaseModel):
    urls: List[str]


class ScrapeResponseBody(BaseModel):
    status: str


class AskRequestBody(BaseModel):
    question: str


class AskResponseBody(BaseModel):
    answer: str = None
