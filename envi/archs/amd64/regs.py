import envi.registers as e_reg
import envi.archs.i386 as e_i386
import envi.archs.amd64 as e_amd64

# NOTE: all REX_R registers must *directly* follow their 3 bit variants
#       in the table below
amd64regs = [
    ("rax",64),("rcx",64),("rdx",64),("rbx",64),("rsp",64),("rbp",64),("rsi",64),("rdi",64),
    # The amd64 extended GP regs
    ("r8",64),("r9",64),("r10",64),("r11",64),("r12",64),("r13",64),("r14",64),("r15",64),

    ("mm0",64),("mm1",64), ("mm2",64), ("mm3",64), ("mm4",64), ("mm5",64), ("mm6",64), ("mm7",64),

    # SIMD registers
    ("xmm0",128),("xmm1",128),("xmm2",128),("xmm3",128),("xmm4",128),("xmm5",128),("xmm6",128),("xmm7",128),
    # The amd64 extended SIMD regs...
    ("xmm8",128),("xmm9",128),("xmm10",128),("xmm11",128),("xmm12",128),("xmm13",128),("xmm14",128),("xmm15",128),

    # Debug registers
    ("debug0",64),("debug1",64),("debug2",64),("debug3",64),("debug4",64),("debug5",64),("debug6",64),("debug7",64),
    # Extended Debug registers (REX.R)
    ("debug8",64),("debug9",64),("debug10",64),("debug11",64),("debug12",64),("debug13",64),("debug14",64),("debug15",64),

    # Control registers
    ("ctrl0",64),("ctrl1",64),("ctrl2",64),("ctrl3",64),("ctrl4",64),("ctrl5",64),("ctrl6",64),("ctrl7",64),
    # Extended Control registers (REX.R)
    ("ctrl8",64),("ctrl9",64),("ctrl10",64),("ctrl11",64),("ctrl12",64),("ctrl13",64),("ctrl14",64),("ctrl15",64),

    # Test registers
    ("test0", 32),("test1", 32),("test2", 32),("test3", 32),("test4", 32),("test5", 32),("test6", 32),("test7", 32),
    # Segment registers
    ("es", 16),("cs",16),("ss",16),("ds",16),("fs",16),("gs",16),
    # FPU Registers
    ("st0", 128),("st1", 128),("st2", 128),("st3", 128),("st4", 128),("st5", 128),("st6", 128),("st7", 128),
    # Leftovers ;)
    ("eflags", 32), ("rip", 64),
]

# Build up a set of accessible constants
l = locals()
e_reg.addLocalEnums(l, amd64regs)

amd64meta = e_i386.i386meta + [
    ("eax", e_amd64.REG_RAX, 0, 32),
    ("ecx", e_amd64.REG_RCX, 0, 32),
    ("edx", e_amd64.REG_RDX, 0, 32),
    ("ebx", e_amd64.REG_RBX, 0, 32),
    ("esp", e_amd64.REG_RSP, 0, 32),
    ("ebp", e_amd64.REG_RBP, 0, 32),
    ("esi", e_amd64.REG_RSI, 0, 32),
    ("edi", e_amd64.REG_RDI, 0, 32),

    ("ax", e_amd64.REG_RAX, 0, 16),
    ("cx", e_amd64.REG_RCX, 0, 16),
    ("dx", e_amd64.REG_RDX, 0, 16),
    ("bx", e_amd64.REG_RBX, 0, 16),
    ("sp", e_amd64.REG_RSP, 0, 16),
    ("bp", e_amd64.REG_RBP, 0, 16),
    ("si", e_amd64.REG_RSI, 0, 16),
    ("di", e_amd64.REG_RDI, 0, 16),

    ("al", e_amd64.REG_RAX, 0, 8),
    ("cl", e_amd64.REG_RCX, 0, 8),
    ("dl", e_amd64.REG_RDX, 0, 8),
    ("bl", e_amd64.REG_RBX, 0, 8),

    ("ah", e_amd64.REG_RAX, 8, 8),
    ("ch", e_amd64.REG_RCX, 8, 8),
    ("dh", e_amd64.REG_RDX, 8, 8),
    ("bh", e_amd64.REG_RBX, 8, 8),

    # NOTE: with a REX prefix, all ah/ch regs get
    # mapped back to being sil/dil etc...
    ("spl", e_amd64.REG_RSP, 8, 8),
    ("bpl", e_amd64.REG_RBP, 8, 8),
    ("sil", e_amd64.REG_RSI, 8, 8),
    ("dil", e_amd64.REG_RDI, 8, 8),

    # The new GP e_amd64.regs are accessible in all modes.
    ("r8d",  e_amd64.REG_R8,  0, 32),
    ("r9d",  e_amd64.REG_R9,  0, 32),
    ("r10d", e_amd64.REG_R10, 0, 32),
    ("r11d", e_amd64.REG_R11, 0, 32),
    ("r12d", e_amd64.REG_R12, 0, 32),
    ("r13d", e_amd64.REG_R13, 0, 32),
    ("r14d", e_amd64.REG_R14, 0, 32),
    ("r15d", e_amd64.REG_R15, 0, 32),

    ("r8w",  e_amd64.REG_R8,  0, 16),
    ("r9w",  e_amd64.REG_R9,  0, 16),
    ("r10w", e_amd64.REG_R10, 0, 16),
    ("r11w", e_amd64.REG_R11, 0, 16),
    ("r12w", e_amd64.REG_R12, 0, 16),
    ("r13w", e_amd64.REG_R13, 0, 16),
    ("r14w", e_amd64.REG_R14, 0, 16),
    ("r15w", e_amd64.REG_R15, 0, 16),

    ("r8l",  e_amd64.REG_R8,  0, 8),
    ("r9l",  e_amd64.REG_R9,  0, 8),
    ("r10l", e_amd64.REG_R10, 0, 8),
    ("r11l", e_amd64.REG_R11, 0, 8),
    ("r12l", e_amd64.REG_R12, 0, 8),
    ("r13l", e_amd64.REG_R13, 0, 8),
    ("r14l", e_amd64.REG_R14, 0, 8),
    ("r15l", e_amd64.REG_R15, 0, 8),

    # Flags
    ("TF", e_amd64.REG_EFLAGS, 8, 1),
]

# Add the meta's indexes
e_reg.addLocalMetas(l, amd64meta)

RMETA_LOW32 = 0x00200000

class Amd64RegisterContext(e_reg.RegisterContext):
    def __init__(self):
        self.loadRegDef(amd64regs)
        self.loadRegMetas(amd64meta)
        self.setRegisterIndexes(e_amd64.REG_RIP, e_amd64.REG_RSP)

    def setRegister(self, index, value):
        # NOTE: A special override is needed here because setting "eax" automagicall
        # zero extends into RAX...
        if (index & 0xffff0000) == RMETA_LOW32:
            index = index & 0xffff
        e_reg.RegisterContext.setRegister(self, index, value)

