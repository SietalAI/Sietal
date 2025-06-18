use thiserror::Error;

#[derive(Error, Debug, Copy, Clone)]
pub enum SietalError {
    #[error("Invalid Instruction")]
    InvalidInstruction,
}
