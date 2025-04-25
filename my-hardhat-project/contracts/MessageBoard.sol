// SPDX-License-Identifier: MIT
pragma solidity ^0.8.28;

contract MessageBoard {
    string private message;
    address public owner;

    event MessageUpdated(string oldMessage, string newMessage);

    constructor(string memory _initialMessage) {
        message = _initialMessage;
        owner = msg.sender;
    }

    function getMessage() public view returns (string memory) {
        return message;
    }

    function updateMessage(string memory _newMessage) public {
        require(msg.sender == owner, "Only owner can update the message");
        emit MessageUpdated(message, _newMessage);
        message = _newMessage;
    }
}
