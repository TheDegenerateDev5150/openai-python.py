# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from openai import OpenAI, AsyncOpenAI
from tests.utils import assert_matches_type
from openai._utils import assert_signatures_in_sync
from openai.types.responses import (
    Response,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestResponses:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create_overload_1(self, client: OpenAI) -> None:
        response = client.responses.create()
        assert_matches_type(Response, response, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_1(self, client: OpenAI) -> None:
        response = client.responses.create(
            background=True,
            include=["code_interpreter_call.outputs"],
            input="string",
            instructions="instructions",
            max_output_tokens=0,
            max_tool_calls=0,
            metadata={"foo": "string"},
            model="gpt-4o",
            parallel_tool_calls=True,
            previous_response_id="previous_response_id",
            prompt={
                "id": "id",
                "variables": {"foo": "string"},
                "version": "version",
            },
            prompt_cache_key="prompt-cache-key-1234",
            reasoning={
                "effort": "low",
                "generate_summary": "auto",
                "summary": "auto",
            },
            safety_identifier="safety-identifier-1234",
            service_tier="auto",
            store=True,
            stream=False,
            temperature=1,
            text={"format": {"type": "text"}},
            tool_choice="none",
            tools=[
                {
                    "name": "name",
                    "parameters": {"foo": "bar"},
                    "strict": True,
                    "type": "function",
                    "description": "description",
                }
            ],
            top_logprobs=0,
            top_p=1,
            truncation="auto",
            user="user-1234",
        )
        assert_matches_type(Response, response, path=["response"])

    @parametrize
    def test_raw_response_create_overload_1(self, client: OpenAI) -> None:
        http_response = client.responses.with_raw_response.create()

        assert http_response.is_closed is True
        assert http_response.http_request.headers.get("X-Stainless-Lang") == "python"
        response = http_response.parse()
        assert_matches_type(Response, response, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_1(self, client: OpenAI) -> None:
        with client.responses.with_streaming_response.create() as http_response:
            assert not http_response.is_closed
            assert http_response.http_request.headers.get("X-Stainless-Lang") == "python"

            response = http_response.parse()
            assert_matches_type(Response, response, path=["response"])

        assert cast(Any, http_response.is_closed) is True

    @parametrize
    def test_method_create_overload_2(self, client: OpenAI) -> None:
        response_stream = client.responses.create(
            stream=True,
        )
        response_stream.response.close()

    @parametrize
    def test_method_create_with_all_params_overload_2(self, client: OpenAI) -> None:
        response_stream = client.responses.create(
            stream=True,
            background=True,
            include=["code_interpreter_call.outputs"],
            input="string",
            instructions="instructions",
            max_output_tokens=0,
            max_tool_calls=0,
            metadata={"foo": "string"},
            model="gpt-4o",
            parallel_tool_calls=True,
            previous_response_id="previous_response_id",
            prompt={
                "id": "id",
                "variables": {"foo": "string"},
                "version": "version",
            },
            prompt_cache_key="prompt-cache-key-1234",
            reasoning={
                "effort": "low",
                "generate_summary": "auto",
                "summary": "auto",
            },
            safety_identifier="safety-identifier-1234",
            service_tier="auto",
            store=True,
            temperature=1,
            text={"format": {"type": "text"}},
            tool_choice="none",
            tools=[
                {
                    "name": "name",
                    "parameters": {"foo": "bar"},
                    "strict": True,
                    "type": "function",
                    "description": "description",
                }
            ],
            top_logprobs=0,
            top_p=1,
            truncation="auto",
            user="user-1234",
        )
        response_stream.response.close()

    @parametrize
    def test_raw_response_create_overload_2(self, client: OpenAI) -> None:
        response = client.responses.with_raw_response.create(
            stream=True,
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = response.parse()
        stream.close()

    @parametrize
    def test_streaming_response_create_overload_2(self, client: OpenAI) -> None:
        with client.responses.with_streaming_response.create(
            stream=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = response.parse()
            stream.close()

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve_overload_1(self, client: OpenAI) -> None:
        response = client.responses.retrieve(
            response_id="resp_677efb5139a88190b512bc3fef8e535d",
        )
        assert_matches_type(Response, response, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params_overload_1(self, client: OpenAI) -> None:
        response = client.responses.retrieve(
            response_id="resp_677efb5139a88190b512bc3fef8e535d",
            include=["code_interpreter_call.outputs"],
            starting_after=0,
            stream=False,
        )
        assert_matches_type(Response, response, path=["response"])

    @parametrize
    def test_raw_response_retrieve_overload_1(self, client: OpenAI) -> None:
        http_response = client.responses.with_raw_response.retrieve(
            response_id="resp_677efb5139a88190b512bc3fef8e535d",
        )

        assert http_response.is_closed is True
        assert http_response.http_request.headers.get("X-Stainless-Lang") == "python"
        response = http_response.parse()
        assert_matches_type(Response, response, path=["response"])

    @parametrize
    def test_streaming_response_retrieve_overload_1(self, client: OpenAI) -> None:
        with client.responses.with_streaming_response.retrieve(
            response_id="resp_677efb5139a88190b512bc3fef8e535d",
        ) as http_response:
            assert not http_response.is_closed
            assert http_response.http_request.headers.get("X-Stainless-Lang") == "python"

            response = http_response.parse()
            assert_matches_type(Response, response, path=["response"])

        assert cast(Any, http_response.is_closed) is True

    @parametrize
    def test_path_params_retrieve_overload_1(self, client: OpenAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `response_id` but received ''"):
            client.responses.with_raw_response.retrieve(
                response_id="",
            )

    @parametrize
    def test_method_retrieve_overload_2(self, client: OpenAI) -> None:
        response_stream = client.responses.retrieve(
            response_id="resp_677efb5139a88190b512bc3fef8e535d",
            stream=True,
        )
        response_stream.response.close()

    @parametrize
    def test_method_retrieve_with_all_params_overload_2(self, client: OpenAI) -> None:
        response_stream = client.responses.retrieve(
            response_id="resp_677efb5139a88190b512bc3fef8e535d",
            stream=True,
            include=["code_interpreter_call.outputs"],
            starting_after=0,
        )
        response_stream.response.close()

    @parametrize
    def test_raw_response_retrieve_overload_2(self, client: OpenAI) -> None:
        response = client.responses.with_raw_response.retrieve(
            response_id="resp_677efb5139a88190b512bc3fef8e535d",
            stream=True,
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = response.parse()
        stream.close()

    @parametrize
    def test_streaming_response_retrieve_overload_2(self, client: OpenAI) -> None:
        with client.responses.with_streaming_response.retrieve(
            response_id="resp_677efb5139a88190b512bc3fef8e535d",
            stream=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = response.parse()
            stream.close()

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve_overload_2(self, client: OpenAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `response_id` but received ''"):
            client.responses.with_raw_response.retrieve(
                response_id="",
                stream=True,
            )

    @parametrize
    def test_method_delete(self, client: OpenAI) -> None:
        response = client.responses.delete(
            "resp_677efb5139a88190b512bc3fef8e535d",
        )
        assert response is None

    @parametrize
    def test_raw_response_delete(self, client: OpenAI) -> None:
        http_response = client.responses.with_raw_response.delete(
            "resp_677efb5139a88190b512bc3fef8e535d",
        )

        assert http_response.is_closed is True
        assert http_response.http_request.headers.get("X-Stainless-Lang") == "python"
        response = http_response.parse()
        assert response is None

    @parametrize
    def test_streaming_response_delete(self, client: OpenAI) -> None:
        with client.responses.with_streaming_response.delete(
            "resp_677efb5139a88190b512bc3fef8e535d",
        ) as http_response:
            assert not http_response.is_closed
            assert http_response.http_request.headers.get("X-Stainless-Lang") == "python"

            response = http_response.parse()
            assert response is None

        assert cast(Any, http_response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: OpenAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `response_id` but received ''"):
            client.responses.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_cancel(self, client: OpenAI) -> None:
        response = client.responses.cancel(
            "resp_677efb5139a88190b512bc3fef8e535d",
        )
        assert_matches_type(Response, response, path=["response"])

    @parametrize
    def test_raw_response_cancel(self, client: OpenAI) -> None:
        http_response = client.responses.with_raw_response.cancel(
            "resp_677efb5139a88190b512bc3fef8e535d",
        )

        assert http_response.is_closed is True
        assert http_response.http_request.headers.get("X-Stainless-Lang") == "python"
        response = http_response.parse()
        assert_matches_type(Response, response, path=["response"])

    @parametrize
    def test_streaming_response_cancel(self, client: OpenAI) -> None:
        with client.responses.with_streaming_response.cancel(
            "resp_677efb5139a88190b512bc3fef8e535d",
        ) as http_response:
            assert not http_response.is_closed
            assert http_response.http_request.headers.get("X-Stainless-Lang") == "python"

            response = http_response.parse()
            assert_matches_type(Response, response, path=["response"])

        assert cast(Any, http_response.is_closed) is True

    @parametrize
    def test_path_params_cancel(self, client: OpenAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `response_id` but received ''"):
            client.responses.with_raw_response.cancel(
                "",
            )


@pytest.mark.parametrize("sync", [True, False], ids=["sync", "async"])
def test_parse_method_in_sync(sync: bool, client: OpenAI, async_client: AsyncOpenAI) -> None:
    checking_client: OpenAI | AsyncOpenAI = client if sync else async_client

    assert_signatures_in_sync(
        checking_client.responses.create,
        checking_client.responses.parse,
        exclude_params={"stream", "tools"},
    )


class TestAsyncResponses:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create_overload_1(self, async_client: AsyncOpenAI) -> None:
        response = await async_client.responses.create()
        assert_matches_type(Response, response, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_1(self, async_client: AsyncOpenAI) -> None:
        response = await async_client.responses.create(
            background=True,
            include=["code_interpreter_call.outputs"],
            input="string",
            instructions="instructions",
            max_output_tokens=0,
            max_tool_calls=0,
            metadata={"foo": "string"},
            model="gpt-4o",
            parallel_tool_calls=True,
            previous_response_id="previous_response_id",
            prompt={
                "id": "id",
                "variables": {"foo": "string"},
                "version": "version",
            },
            prompt_cache_key="prompt-cache-key-1234",
            reasoning={
                "effort": "low",
                "generate_summary": "auto",
                "summary": "auto",
            },
            safety_identifier="safety-identifier-1234",
            service_tier="auto",
            store=True,
            stream=False,
            temperature=1,
            text={"format": {"type": "text"}},
            tool_choice="none",
            tools=[
                {
                    "name": "name",
                    "parameters": {"foo": "bar"},
                    "strict": True,
                    "type": "function",
                    "description": "description",
                }
            ],
            top_logprobs=0,
            top_p=1,
            truncation="auto",
            user="user-1234",
        )
        assert_matches_type(Response, response, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_1(self, async_client: AsyncOpenAI) -> None:
        http_response = await async_client.responses.with_raw_response.create()

        assert http_response.is_closed is True
        assert http_response.http_request.headers.get("X-Stainless-Lang") == "python"
        response = http_response.parse()
        assert_matches_type(Response, response, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_1(self, async_client: AsyncOpenAI) -> None:
        async with async_client.responses.with_streaming_response.create() as http_response:
            assert not http_response.is_closed
            assert http_response.http_request.headers.get("X-Stainless-Lang") == "python"

            response = await http_response.parse()
            assert_matches_type(Response, response, path=["response"])

        assert cast(Any, http_response.is_closed) is True

    @parametrize
    async def test_method_create_overload_2(self, async_client: AsyncOpenAI) -> None:
        response_stream = await async_client.responses.create(
            stream=True,
        )
        await response_stream.response.aclose()

    @parametrize
    async def test_method_create_with_all_params_overload_2(self, async_client: AsyncOpenAI) -> None:
        response_stream = await async_client.responses.create(
            stream=True,
            background=True,
            include=["code_interpreter_call.outputs"],
            input="string",
            instructions="instructions",
            max_output_tokens=0,
            max_tool_calls=0,
            metadata={"foo": "string"},
            model="gpt-4o",
            parallel_tool_calls=True,
            previous_response_id="previous_response_id",
            prompt={
                "id": "id",
                "variables": {"foo": "string"},
                "version": "version",
            },
            prompt_cache_key="prompt-cache-key-1234",
            reasoning={
                "effort": "low",
                "generate_summary": "auto",
                "summary": "auto",
            },
            safety_identifier="safety-identifier-1234",
            service_tier="auto",
            store=True,
            temperature=1,
            text={"format": {"type": "text"}},
            tool_choice="none",
            tools=[
                {
                    "name": "name",
                    "parameters": {"foo": "bar"},
                    "strict": True,
                    "type": "function",
                    "description": "description",
                }
            ],
            top_logprobs=0,
            top_p=1,
            truncation="auto",
            user="user-1234",
        )
        await response_stream.response.aclose()

    @parametrize
    async def test_raw_response_create_overload_2(self, async_client: AsyncOpenAI) -> None:
        response = await async_client.responses.with_raw_response.create(
            stream=True,
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = response.parse()
        await stream.close()

    @parametrize
    async def test_streaming_response_create_overload_2(self, async_client: AsyncOpenAI) -> None:
        async with async_client.responses.with_streaming_response.create(
            stream=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = await response.parse()
            await stream.close()

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve_overload_1(self, async_client: AsyncOpenAI) -> None:
        response = await async_client.responses.retrieve(
            response_id="resp_677efb5139a88190b512bc3fef8e535d",
        )
        assert_matches_type(Response, response, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params_overload_1(self, async_client: AsyncOpenAI) -> None:
        response = await async_client.responses.retrieve(
            response_id="resp_677efb5139a88190b512bc3fef8e535d",
            include=["code_interpreter_call.outputs"],
            starting_after=0,
            stream=False,
        )
        assert_matches_type(Response, response, path=["response"])

    @parametrize
    async def test_raw_response_retrieve_overload_1(self, async_client: AsyncOpenAI) -> None:
        http_response = await async_client.responses.with_raw_response.retrieve(
            response_id="resp_677efb5139a88190b512bc3fef8e535d",
        )

        assert http_response.is_closed is True
        assert http_response.http_request.headers.get("X-Stainless-Lang") == "python"
        response = http_response.parse()
        assert_matches_type(Response, response, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve_overload_1(self, async_client: AsyncOpenAI) -> None:
        async with async_client.responses.with_streaming_response.retrieve(
            response_id="resp_677efb5139a88190b512bc3fef8e535d",
        ) as http_response:
            assert not http_response.is_closed
            assert http_response.http_request.headers.get("X-Stainless-Lang") == "python"

            response = await http_response.parse()
            assert_matches_type(Response, response, path=["response"])

        assert cast(Any, http_response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve_overload_1(self, async_client: AsyncOpenAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `response_id` but received ''"):
            await async_client.responses.with_raw_response.retrieve(
                response_id="",
            )

    @parametrize
    async def test_method_retrieve_overload_2(self, async_client: AsyncOpenAI) -> None:
        response_stream = await async_client.responses.retrieve(
            response_id="resp_677efb5139a88190b512bc3fef8e535d",
            stream=True,
        )
        await response_stream.response.aclose()

    @parametrize
    async def test_method_retrieve_with_all_params_overload_2(self, async_client: AsyncOpenAI) -> None:
        response_stream = await async_client.responses.retrieve(
            response_id="resp_677efb5139a88190b512bc3fef8e535d",
            stream=True,
            include=["code_interpreter_call.outputs"],
            starting_after=0,
        )
        await response_stream.response.aclose()

    @parametrize
    async def test_raw_response_retrieve_overload_2(self, async_client: AsyncOpenAI) -> None:
        response = await async_client.responses.with_raw_response.retrieve(
            response_id="resp_677efb5139a88190b512bc3fef8e535d",
            stream=True,
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = response.parse()
        await stream.close()

    @parametrize
    async def test_streaming_response_retrieve_overload_2(self, async_client: AsyncOpenAI) -> None:
        async with async_client.responses.with_streaming_response.retrieve(
            response_id="resp_677efb5139a88190b512bc3fef8e535d",
            stream=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = await response.parse()
            await stream.close()

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve_overload_2(self, async_client: AsyncOpenAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `response_id` but received ''"):
            await async_client.responses.with_raw_response.retrieve(
                response_id="",
                stream=True,
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncOpenAI) -> None:
        response = await async_client.responses.delete(
            "resp_677efb5139a88190b512bc3fef8e535d",
        )
        assert response is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncOpenAI) -> None:
        http_response = await async_client.responses.with_raw_response.delete(
            "resp_677efb5139a88190b512bc3fef8e535d",
        )

        assert http_response.is_closed is True
        assert http_response.http_request.headers.get("X-Stainless-Lang") == "python"
        response = http_response.parse()
        assert response is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncOpenAI) -> None:
        async with async_client.responses.with_streaming_response.delete(
            "resp_677efb5139a88190b512bc3fef8e535d",
        ) as http_response:
            assert not http_response.is_closed
            assert http_response.http_request.headers.get("X-Stainless-Lang") == "python"

            response = await http_response.parse()
            assert response is None

        assert cast(Any, http_response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncOpenAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `response_id` but received ''"):
            await async_client.responses.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_cancel(self, async_client: AsyncOpenAI) -> None:
        response = await async_client.responses.cancel(
            "resp_677efb5139a88190b512bc3fef8e535d",
        )
        assert_matches_type(Response, response, path=["response"])

    @parametrize
    async def test_raw_response_cancel(self, async_client: AsyncOpenAI) -> None:
        http_response = await async_client.responses.with_raw_response.cancel(
            "resp_677efb5139a88190b512bc3fef8e535d",
        )

        assert http_response.is_closed is True
        assert http_response.http_request.headers.get("X-Stainless-Lang") == "python"
        response = http_response.parse()
        assert_matches_type(Response, response, path=["response"])

    @parametrize
    async def test_streaming_response_cancel(self, async_client: AsyncOpenAI) -> None:
        async with async_client.responses.with_streaming_response.cancel(
            "resp_677efb5139a88190b512bc3fef8e535d",
        ) as http_response:
            assert not http_response.is_closed
            assert http_response.http_request.headers.get("X-Stainless-Lang") == "python"

            response = await http_response.parse()
            assert_matches_type(Response, response, path=["response"])

        assert cast(Any, http_response.is_closed) is True

    @parametrize
    async def test_path_params_cancel(self, async_client: AsyncOpenAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `response_id` but received ''"):
            await async_client.responses.with_raw_response.cancel(
                "",
            )
