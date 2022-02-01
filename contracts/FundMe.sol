// SPDX License Identifier: MIT
pragma solidity >=0.6.0 <=0.9.0;
import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";

contract FundMe {
    address public owner;
    mapping(address => uint256) public addressToAmountFunded;
    address[] public funder;
    AggregatorV3Interface public priceFeed;

    constructor(address _PriceFeed) public {
        priceFeed = AggregatorV3Interface(_PriceFeed);
        owner = msg.sender;
    }

    function fund() public payable {
        uint256 minUsd = 50;
        //require(getConversionRate(msg.value) >= minUsd, "Low Eth!");
        addressToAmountFunded[msg.sender] += msg.value;
        funder.push(msg.sender);
    }

    /*  function getVersion() public view returns (uint256) {
        AggregatorV3Interface priceFeed = AggregatorV3Interface(
            0x9326BFA02ADD2366b30bacB125260Af641031331
        );
        return priceFeed.version();
    }*/
    function getEntranceFee() public view returns (uint256) {
        uint256 minUSD = 50 * 10**10;
        uint256 price = getPrice();
        uint256 precision = 1 * 10**18;
        return (minUSD * precision) / price;
    }

    function getPrice() public view returns (uint256) {
        (, int256 answer, , , ) = priceFeed.latestRoundData();
        return uint256(answer);
    }

    function getConversionRate(uint256 etherIn) public view returns (uint256) {
        uint256 EthToUsd = getPrice();
        return (etherIn * EthToUsd) / 100000000;
    }

    modifier OwnerOnly() {
        require(msg.sender == owner);
        _;
    }

    function withdraw() public payable OwnerOnly {
        payable(msg.sender).transfer(address(this).balance);
        for (
            uint256 funderIndex = 0;
            funderIndex > funder.length;
            funderIndex++
        ) {
            address funders = funder[funderIndex];
            addressToAmountFunded[funders] = 0;
        }
        funder = new address[](0);
    }
}
