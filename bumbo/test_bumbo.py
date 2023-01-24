# test_bumbo.py

import pytest


def test_bumbo_test_client_can_send_requests(api, client):
    RESPONSE_TEXT = "THIS IS COOL"
    
    @api.route("/hey")
    def cool(req, resp):
        resp.text = RESPONSE_TEXT
    
    assert client.get("http://testserver/hey").text == RESPONSE_TEXT


def test_basic_route_adding(api):
    @api.route("/home")
    def home(req, resp):
        resp.text = "YOLO"


def test_route_overlap_throws_exception(api):
    @api.route("/home")
    def home(req, resp):
        resp.text = "YOLO"
    
    with pytest.raises(AssertionError):
        @api.route("/home")
        def home2(req, resp):
            resp.text = "YOLO"


