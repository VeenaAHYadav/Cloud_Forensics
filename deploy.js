async function main() {
    const Contract = await ethers.getContractFactory("Forensics");

    const contract = await Contract.deploy();

    await contract.waitForDeployment();

    console.log("🚀 Sepolia Contract deployed at:", await contract.getAddress());
}

main().catch((error) => {
    console.error(error);
    process.exitCode = 1;
});