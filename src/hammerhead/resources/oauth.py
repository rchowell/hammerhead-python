# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import oauth_authorize_params, oauth_deauthorize_params, oauth_exchange_token_params
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.oauth_exchange_token_response import OAuthExchangeTokenResponse

__all__ = ["OAuthResource", "AsyncOAuthResource"]


class OAuthResource(SyncAPIResource):
    """
    Access to our API is authorized using the [OAuth 2.0](https://datatracker.ietf.org/doc/html/rfc6749) authorization framework.

    To get started, you will need to create an API Client and obtain a client ID and secret.

    Users can then be authorized by providing a link to our authorization url:

    ```html
    <a href="https://api.hammerhead.io/v1/auth/oauth/authorize
      ?client_id={client_id}
      &redirect_uri={redirect_uri}
      &response_type=code
      &scope={scope}
      &state={state}"
    />
    ```

    This will redirect users to our OAuth Confirm page where users will be allowed to
    select a subset of scopes from the ones requested. Scopes should be space delimited.

    On deny, users will be sent to the `redirect_uri` with an error set:

    ```
    {redirect_uri}?error=access_denied&state={state}
    ```

    On accept, users accounts will be linked with the selected scopes and will be sent to
    the `redirect_uri` with the auth code and state:

    ```
    {redirect_uri}?code={code}&state={state}
    ```

    Once code and state are received, they can be exchanged for an access token using the `/oauth/token` endpoint.

    This bearer token can then be used to access our API endpoints.
    """

    @cached_property
    def with_raw_response(self) -> OAuthResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/rchowell/hammerhead-python#accessing-raw-response-data-eg-headers
        """
        return OAuthResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OAuthResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/rchowell/hammerhead-python#with_streaming_response
        """
        return OAuthResourceWithStreamingResponse(self)

    def authorize(
        self,
        *,
        client_id: str,
        redirect_uri: str,
        response_type: Literal["code"],
        scope: str,
        state: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Authorize redirect endpoint to obtain consent from users.

        Args:
          client_id: Your client ID

          redirect_uri: Should match one of your configured redirect endpoints

          response_type: OAuth response type

          scope: Space delimited scopes being requested

          state: Opaque value passed back in the redirect

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/oauth/authorize"
            if self._client._base_url_overridden
            else "https://api.hammerhead.io/v1/auth/oauth/authorize",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "client_id": client_id,
                        "redirect_uri": redirect_uri,
                        "response_type": response_type,
                        "scope": scope,
                        "state": state,
                    },
                    oauth_authorize_params.OAuthAuthorizeParams,
                ),
            ),
            cast_to=NoneType,
        )

    def deauthorize(
        self,
        *,
        token: str,
        client_id: str,
        client_secret: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Remove a user's account link, all of their imported routes and workouts, and
        removes their current refresh tokens.

        Args:
          token: An access token for the user to deauthorize

          client_id: Your client ID

          client_secret: Your client secret

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/oauth/deauthorize"
            if self._client._base_url_overridden
            else "https://api.hammerhead.io/v1/auth/oauth/deauthorize",
            body=maybe_transform(
                {
                    "token": token,
                    "client_id": client_id,
                    "client_secret": client_secret,
                },
                oauth_deauthorize_params.OAuthDeauthorizeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def exchange_token(
        self,
        *,
        client_id: str,
        client_secret: str,
        grant_type: Literal["authorization_code", "refresh_token"],
        code: str | Omit = omit,
        redirect_uri: str | Omit = omit,
        refresh_token: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OAuthExchangeTokenResponse:
        """
        Exchange authorization codes or refresh tokens for a new bearer token.

        Args:
          client_id: Your client ID

          client_secret: Your client secret

          grant_type: OAuth grant type

          code: Required for code auth, generated from initial authorize request

          redirect_uri: Required for code auth, should match the `redirect_uri` from the authorize
              request

          refresh_token: Required for code auth, generated from previous token request

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/oauth/token" if self._client._base_url_overridden else "https://api.hammerhead.io/v1/auth/oauth/token",
            body=maybe_transform(
                {
                    "client_id": client_id,
                    "client_secret": client_secret,
                    "grant_type": grant_type,
                    "code": code,
                    "redirect_uri": redirect_uri,
                    "refresh_token": refresh_token,
                },
                oauth_exchange_token_params.OAuthExchangeTokenParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OAuthExchangeTokenResponse,
        )


class AsyncOAuthResource(AsyncAPIResource):
    """
    Access to our API is authorized using the [OAuth 2.0](https://datatracker.ietf.org/doc/html/rfc6749) authorization framework.

    To get started, you will need to create an API Client and obtain a client ID and secret.

    Users can then be authorized by providing a link to our authorization url:

    ```html
    <a href="https://api.hammerhead.io/v1/auth/oauth/authorize
      ?client_id={client_id}
      &redirect_uri={redirect_uri}
      &response_type=code
      &scope={scope}
      &state={state}"
    />
    ```

    This will redirect users to our OAuth Confirm page where users will be allowed to
    select a subset of scopes from the ones requested. Scopes should be space delimited.

    On deny, users will be sent to the `redirect_uri` with an error set:

    ```
    {redirect_uri}?error=access_denied&state={state}
    ```

    On accept, users accounts will be linked with the selected scopes and will be sent to
    the `redirect_uri` with the auth code and state:

    ```
    {redirect_uri}?code={code}&state={state}
    ```

    Once code and state are received, they can be exchanged for an access token using the `/oauth/token` endpoint.

    This bearer token can then be used to access our API endpoints.
    """

    @cached_property
    def with_raw_response(self) -> AsyncOAuthResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/rchowell/hammerhead-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOAuthResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOAuthResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/rchowell/hammerhead-python#with_streaming_response
        """
        return AsyncOAuthResourceWithStreamingResponse(self)

    async def authorize(
        self,
        *,
        client_id: str,
        redirect_uri: str,
        response_type: Literal["code"],
        scope: str,
        state: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Authorize redirect endpoint to obtain consent from users.

        Args:
          client_id: Your client ID

          redirect_uri: Should match one of your configured redirect endpoints

          response_type: OAuth response type

          scope: Space delimited scopes being requested

          state: Opaque value passed back in the redirect

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/oauth/authorize"
            if self._client._base_url_overridden
            else "https://api.hammerhead.io/v1/auth/oauth/authorize",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "client_id": client_id,
                        "redirect_uri": redirect_uri,
                        "response_type": response_type,
                        "scope": scope,
                        "state": state,
                    },
                    oauth_authorize_params.OAuthAuthorizeParams,
                ),
            ),
            cast_to=NoneType,
        )

    async def deauthorize(
        self,
        *,
        token: str,
        client_id: str,
        client_secret: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Remove a user's account link, all of their imported routes and workouts, and
        removes their current refresh tokens.

        Args:
          token: An access token for the user to deauthorize

          client_id: Your client ID

          client_secret: Your client secret

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/oauth/deauthorize"
            if self._client._base_url_overridden
            else "https://api.hammerhead.io/v1/auth/oauth/deauthorize",
            body=await async_maybe_transform(
                {
                    "token": token,
                    "client_id": client_id,
                    "client_secret": client_secret,
                },
                oauth_deauthorize_params.OAuthDeauthorizeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def exchange_token(
        self,
        *,
        client_id: str,
        client_secret: str,
        grant_type: Literal["authorization_code", "refresh_token"],
        code: str | Omit = omit,
        redirect_uri: str | Omit = omit,
        refresh_token: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OAuthExchangeTokenResponse:
        """
        Exchange authorization codes or refresh tokens for a new bearer token.

        Args:
          client_id: Your client ID

          client_secret: Your client secret

          grant_type: OAuth grant type

          code: Required for code auth, generated from initial authorize request

          redirect_uri: Required for code auth, should match the `redirect_uri` from the authorize
              request

          refresh_token: Required for code auth, generated from previous token request

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/oauth/token" if self._client._base_url_overridden else "https://api.hammerhead.io/v1/auth/oauth/token",
            body=await async_maybe_transform(
                {
                    "client_id": client_id,
                    "client_secret": client_secret,
                    "grant_type": grant_type,
                    "code": code,
                    "redirect_uri": redirect_uri,
                    "refresh_token": refresh_token,
                },
                oauth_exchange_token_params.OAuthExchangeTokenParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OAuthExchangeTokenResponse,
        )


class OAuthResourceWithRawResponse:
    def __init__(self, oauth: OAuthResource) -> None:
        self._oauth = oauth

        self.authorize = to_raw_response_wrapper(
            oauth.authorize,
        )
        self.deauthorize = to_raw_response_wrapper(
            oauth.deauthorize,
        )
        self.exchange_token = to_raw_response_wrapper(
            oauth.exchange_token,
        )


class AsyncOAuthResourceWithRawResponse:
    def __init__(self, oauth: AsyncOAuthResource) -> None:
        self._oauth = oauth

        self.authorize = async_to_raw_response_wrapper(
            oauth.authorize,
        )
        self.deauthorize = async_to_raw_response_wrapper(
            oauth.deauthorize,
        )
        self.exchange_token = async_to_raw_response_wrapper(
            oauth.exchange_token,
        )


class OAuthResourceWithStreamingResponse:
    def __init__(self, oauth: OAuthResource) -> None:
        self._oauth = oauth

        self.authorize = to_streamed_response_wrapper(
            oauth.authorize,
        )
        self.deauthorize = to_streamed_response_wrapper(
            oauth.deauthorize,
        )
        self.exchange_token = to_streamed_response_wrapper(
            oauth.exchange_token,
        )


class AsyncOAuthResourceWithStreamingResponse:
    def __init__(self, oauth: AsyncOAuthResource) -> None:
        self._oauth = oauth

        self.authorize = async_to_streamed_response_wrapper(
            oauth.authorize,
        )
        self.deauthorize = async_to_streamed_response_wrapper(
            oauth.deauthorize,
        )
        self.exchange_token = async_to_streamed_response_wrapper(
            oauth.exchange_token,
        )
