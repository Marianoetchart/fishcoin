contract tokenRecipient { function receiveApproval(address _from, uint256 _value, address _token,bytes _extraData); }

contract FishCoins{
    /* Public variables of the FishCoins */
    string public name;
    string public symbol;
    string public version;
    uint256 public totalFishSupply;
    uint8 public decimals;

    /* track the fishcoin account holders */
    mapping (address => uint256) public balanceOf;
    mapping (address => mapping (address => uint256)) public allowance;
    mapping (address => mapping (address => uint256)) public spentAllowance;

    /* Generates a public event on the blockchain that will notify clients */
    event Transfer(address indexed from, address indexed to, uint256 value);

    /* define the creation of coins at startup*/
    function FishCoins(uint256 initialCatchSize,
                  string fishCoinType,
                  uint8 decimalPlaces,
                  string fishCoinSymbol,
                  string versionOfTheCode){
      balanceOf[msg.sender] = initialCatchSize;           // fisherman gets all initial tokens
      totalFishSupply = initialCatchSize;
      name = fishCoinType;                                   // Set the name for display purposes
      symbol = fishCoinSymbol;                               // Set the symbol for display purposes
      decimals = decimalPlaces;                            // Amount of decimals for display purposes
      version = versionOfTheCode;
  }

    /* send coins */
    function transfer(address _to, uint256 _value) {
    /* check if sender has enough fishcoin & check for overflows */
    if (balanceOf[msg.sender] < _value) throw;           // Check if the sender has enough
    if (balanceOf[_to] + _value < balanceOf[_to]) throw; // Check for overflows

    /* Add and subtract new balances */
    balanceOf[msg.sender] -= _value;
    balanceOf[_to] += _value;

    /* Notify anyone listening that this transfer took place */
    Transfer(msg.sender, _to, _value);
  }

  /* Allow another contract to spend some fishCoins in your behalf */
   function approveAndCall(address _spender, uint256 _value, bytes _extraData)
       returns (bool success) {
       allowance[msg.sender][_spender] = _value;
       tokenRecipient spender = tokenRecipient(_spender);
       spender.receiveApproval(msg.sender, _value, this, _extraData);
       return true;
   }

   /* A contract attempts to get the fishCoins */
   function transferFrom(address _from, address _to, uint256 _value) returns (bool success) {
       if (balanceOf[_from] < _value) throw;                 // Check if the sender has enough
       if (balanceOf[_to] + _value < balanceOf[_to]) throw;  // Check for overflows
       if (spentAllowance[_from][msg.sender] + _value > allowance[_from][msg.sender]) throw;   // Check allowance
       balanceOf[_from] -= _value;                          // Subtract from the sender
       balanceOf[_to] += _value;                            // Add the same to the recipient
       spentAllowance[_from][msg.sender] += _value;
       Transfer(_from, _to, _value);
       return true;
   }

   /* This unnamed function is called whenever someone tries to send ether to it */
   function () {
       throw;     // Prevents accidental sending of ether
   }

   /* currently adding */
   //fish lifespan
   //notify monitoring body if exceptions are thrown
   //combination logic (trakcing lifetime of fish products)
}
