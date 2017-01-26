#! /usr/bin/env python
# encoding: utf-8

from __future__ import absolute_import

import os
import io
import requests.exceptions
from .exceptions import *

try:
    basestring
except NameError:
    basestring = str

class TagsMixin(object):
    """Functionality for manipulating tags on a Vimeo video.
    """
    TAGS_ENDPOINT = '/videos/{video_id}/tags'

    def set_tags(self, video_id, video_tags):
        """Set tags for the given uri."""
        uri = self.TAGS_ENDPOINT.format(video_id=video_id)

        response = self.put(uri, data=video_tags)

        if response.status_code >= 400:
            raise TagSetFailure(response, "Failed to set a tag with Vimeo")


class CategoriesMixin(object):
    """Functionality for manipulating categories on a Vimeo video.
    """
    CATEGORIES_ENDPOINT = '/videos/{video_id}/categories'

    def set_categories(self, video_id, video_categories):
        """Set categories for the given uri."""
        uri = self.CATEGORIES_ENDPOINT.format(video_id=video_id)

        response = self.put(uri, data=video_categories)

        if response.status_code >= 400:
            raise CategoriesSetFailure(response, "Failed to set categories with Vimeo")


class ChannelsMixin(object):
    """Functionality for putting Vimeo video in a channel.
    """
    CHANNELS_ENDPOINT = '/channels/{channel_id}/videos/{video_id}'

    def add_to_channel(self, video_id, channel_id):
        """Put a video in a channel."""
        uri = self.CHANNELS_ENDPOINT.format(video_id=video_id, channel_id=channel_id)

        response = self.put(uri)

        if response.status_code >= 400:
            raise AddToChannelFailure(response, "Failed to put a video in a channel with Vimeo")


class CreditsMixin(object):
    """Functionality for manipulating credits on a Vimeo video.
    """
    CREDITS_ADD_ENDPOINT = '/videos/{video_id}/credits'

    def add_credit(self, video_id, role, name, email, usr_id=""):
        """Set categories for the given uri."""
        uri = self.CREDITS_ADD_ENDPOINT.format(video_id=video_id)

        if usr_id:
            response = self.post(uri, data={'role':role,
                'user_uri': "/users/%s" % usr_id,
                'email':email})
        else:
            response = self.post(uri, data={'role':role,
                'name':name,
                'email':email})

        if response.status_code >= 400:
            raise AddCreditsFailure(response, "Failed to add credit with Vimeo")


class EmbedMixin(object):
    """Functionality for manipulating embed settings on a Vimeo video.
    """
    EMBED_PRESET_ENDPOINT = '/videos/{video_id}/presets/{preset_id}'

    def set_embed_preset(self, video_id, preset_id):
        """Set categories for the given uri."""
        uri = self.EMBED_PRESET_ENDPOINT.format(video_id=video_id, preset_id=preset_id)

        response = self.put(uri)

        print(response)

        if response.status_code >= 400:
            raise SetEmbedPresetFailure(response, "Failed to set embed preset with Vimeo")


class UpdateMixin(TagsMixin, CategoriesMixin, ChannelsMixin, CreditsMixin, EmbedMixin):
    """Handle editing video properties using the Vimeo API."""
    pass
