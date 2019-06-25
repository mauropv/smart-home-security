pragma solidity ^0.5.1;

import "./SafeMath.sol";


contract SDBB {
    using SafeMath for uint;

    event NewRule (address sender, address source, address dest, string action);

    struct Rule{
        address source;
        address dest;
        string action;
        bool active;
    }

    Rule[] public rules;

    mapping (uint => address) public ruleToOwner;
    mapping (address => uint) ownerRuleCount;



    function getRulesByOwner(address _owner) external view returns( uint[] memory) {
        uint[] memory result = new uint[](ownerRuleCount[_owner]);
        uint counter = 0;
        for (uint i = 0; i < rules.length; i++) {
            if (ruleToOwner[i] == _owner) {
                result[counter] = i;
                counter++;
            }
        }
        return result;
    }

    function createRule(address  _source, address  _dest, string memory _action) public {
        uint id = rules.push(Rule(_source, _dest, _action, true)) - 1;
        ruleToOwner[id] = msg.sender;
        ownerRuleCount[msg.sender] = ownerRuleCount[msg.sender].add(1);
        emit NewRule(msg.sender, _source, _dest, _action);
    }
   
}
