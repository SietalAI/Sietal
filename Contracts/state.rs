use solana_program::pubkey::Pubkey;
use serde::{Deserialize, Serialize};

#[derive(Serialize, Deserialize, Debug)]
pub struct AgentData {
    pub owner: Pubkey,
    pub preferences: Vec<u8>,
}
