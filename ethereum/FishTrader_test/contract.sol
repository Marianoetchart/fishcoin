//Sample contract
contract Sample
{
	uint value;
	function Sample(uint v) {
		value = v;
	}
	function set(uint v) {
		value = v;
	}
	function get() constant returns (uint) {
		return value;
	}
}

//Rating contract
contract Rating {
	function setRating(bytes32 _key, uint256 _value) {
		ratings[_key] = _value;
	}
	mapping (bytes32 => uint256) public ratings;
}