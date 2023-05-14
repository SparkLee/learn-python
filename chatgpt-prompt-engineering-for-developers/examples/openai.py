#!/bin/python
# -*- coding: utf-8 -*-

import openai
import os
# from dotenv import load_dotenv, find_dotenv

# _ = load_dotenv(find_dotenv())

openai.api_key = os.getenv('OPENAI_API_KEY')