---
title: "术语表"
url: "/terms"
weight: 1
---

(page_terms)=

术语表

---

[0-9](@term_09) | [A](@term_a) | [B](@term_b) | [C](@term_c) | [D](@term_d) | [E](@term_e) | [F](@term_f) | [G](@term_g) | [H](@term_h) | [I](@term_i) | [J](@term_j) | [K](@term_k) | [L](@term_l) | [M](@term_m) | [N](@term_n) | [O](@term_o) | [P](@term_p) | [Q](@term_q) | [R](@term_r) | [S](@term_s) | [T](@term_t) | [U](@term_u) | [V](@term_v) | [W](@term_w) | [X](@term_x) | [Y](@term_y) | [Z](@term_z)

---

## 0

(term_09)=

## A

(term_a)=

### AAA

(aaa)=

Authentication, Authorization, and Accounting

详见 [RADIUS](@radius)

### AARCH64

64-bit ARM hardware (chip) architecture. Informally knows as "ARM 64".

### ACM

(acm)=

Authenticated Code Module

firmware 上供 CPU 加载执行的一段验证程序，CPU 会使用内置的公钥校验 ACM 的签名。
ACM 会负责校验执行 [IBB](@ibb)，从而启动 boot。

### ADPPA

美国数据隐私和保护法，American Data Privacy and Protection Act

- <https://www.congress.gov/bill/117th-congress/house-bill/8152/text>

第一部联邦层面的数据保护法，此前都是州法，如：

- CCPA 加州消费者隐私法案
- CDPA 弗吉尼亚州消费者数据保护法

### AMD APU

(amd_apu)=

AMD Accelerated Processing Unit

- [从 AMD APU 的名存实亡谈起](https://www.eet-china.com/news/202108190817.html)

AMD 在 2006 年提出的构想，将 GPU 和 CPU 融合到同一个芯片内，共享同一个内存空间，
这也被称为[异构架构](@hsa)。

### AMD EPYC

(amd_epyc)=

AMD 霄龙处理器

### AMD fTPM

(amd_ftpm)=

AMD Firmware Trusted Platform Module

AMD 通过加密芯片模拟 [TPM 2.0](@tpm)。

对标 [Intel PTT](@intel_ptt)

### AMD JPEG

(amd_jpeg)=

AMD Joint Photographic Experts Group

### AMD NPT

(term_amd_npt)=

AMD Nested Page Tables

- [AMD-V™ Nested Paging.pdf](https://1drv.ms/b/s!Au45o0W1gVVLusNwYkhQ2Ts_tvAJMQ?e=pZ0hjo)

属于 [AMD-V](@term_amd_v) 的一部分。

负责虚拟机内存地址到物理地址的转换：

```plaintext
GVA --> GPA  --> HPA
```

### AMD PSP

(psp)=

AMD Platform Security Processor

AMD 内负责为 [SME](@term_amd_sme) 生成密钥和管理的协处理器。

同义词：[AMD SP](@amd_sp)

### AMD RVI

(term_amd_rvi)=

AMD Rapid Virtualization Indexing

AMD 对 [SLAT](@term_slat) 的实现。
属于 [AMD-V](@term_amd_v) 的一部分。

### AMD SDMA

(term_amd_sdma)=

AMD System DMA

### AMD SEV

(amd-sev)=

AMD Secure Encrypted Virtualization

AMD 2016 年为虚拟机提供的内存加密隔离方案，每个虚拟机都用唯一的密钥进行加密。

[Read More...](@page_secure_vm_sev)

### AMD SEV AE

(amd_sev_ae)=

AMD SEV Automatic Exits

[Read More...](@ame_sev_exit)

### AMD SEV ARK

(amd_ark)=

AMD Root Key

每一代 AMD 产品都会有一个 ARK 来签发所有的硬件证书（如 `Milan`），
用于签发 [ASK](@amd_ask)。

![keys](https://s3.laisky.com/uploads/2022/10/amd-keys.drawio.png)

### AMD SEV ASK

(amd_ask)=

AMD SEV Signing Key

用于签发 [CEK](@amd_cek)，由 [ARK](@amd_ark) 签发。

看上去和 ARK 一样，也是一代产品（如 `Milan`）共用一个 ARK。

### AMD SEV CEK

(amd_cek)=

AMD SEV Chip Endorsement Key

签发 [PEK](@amd_pek)，由 [ASK](@amd_ask) 签发。

### AMD SEV-ES

(amd-sev-es)=

AMD Secure Encrypted Virtualization-Encrypted State

2017 年，AMD 为增强 [SEV](@amd-sev) 安全性提出的方案。
为虚拟机寄存器提供额外的保护。

当虚拟机停止运行时，对所有 CPU 寄存器内容进行加密。
这可以防止 CPU 寄存器中的信息泄露给管理程序等组件，甚至可以检测到对 CPU 寄存器状态的恶意修改。

### AMD SEV GHCB

(amd_sev_ghcb)=

AMD SEV Guest-Hypervisor Communication Block

[Read More...](@amd_snp_ghcb)

### AMD SEV IDB

(amd_sev_idb)=

AMD SEV Identity Block

在 SNP CVM 启动时，可以传入一个 IDB，包含 CVM 的度量值和 UUID。

IDB 将会出现在 SNP REPORT 中。

### AMD SEV KDS

AMD SEV Key Distribution System

AMD 负责保管和签发 [ASK](@amd_ask) 的基础设施。

### AMD SEV KEK

AMD SEV Key Encryption Key

### AMD SEV KIK

AMD SEV Key Integrity Key

### AMD SEV MA

(amd_sev_ma)=

AMD SEV Migration Agent

本身也是一个 SEV SNP CVM。

同一 Host 上的 CVM 可以关联到 MA。CVM 和 MA 是多对一的关系。

不同宿主机上的 MA 负责协商 CVM 的迁移。

### AMD SEV NAE

(amd_sev_nae)=

AMD SEV Non-Automatic Exits

一切非 [AE](@amd_sev_ae) 的异常，将会导致 `#VC` 异常。

[Read More...](@ame_sev_exit)

### AMD SEV OCA

(amd_oca)=

AMD SEV Owner Certificate Authority

用于签发 [PEK](@amd_pek)。

### AMD SEV PDH

(amd_pdh)=

AMD SEV Platform Diffie-Hellman

被 [PEK](@amd_pek) 签发。

### AMD SEV PEK

(amd_pek)=

AMD SEV Platform Endorsement Key

用于签发 [PDH](@amd_pdh)，由 [CEK](amd_cek) 和 [OCA](amd_oca) 签发

### AMD SEV RMP

(amd_rmp)=

AMD Reverse Map Table

AMD 为保护虚拟机内存完整性提供的解决方案。

[Read More...](@amd_snp_rmp)

### AMD SEV-SNP

(amd_sev_snp)=

AMD SEV Secure Nested Paging

- [AMD SEV-SNP- Strengthening VM Isolation with Integrity Protection and More.pdf](https://1drv.ms/b/s!Au45o0W1gVVLutdDDRh0G6_IEbiqTw?e=V66FdY)

AMD 的新一代 [CVM](@cvm) 方案（相较于上一代的 [SEV](@amd-sev)）。

为虚拟机提供[内存](@term_amd_npt)一致性的安全保护。
主要实现技术是 [RMP](@amd_rmp) 和 Page Validation。

Page Validation 通过在 [RMP](@amd_rmp) 中为每一物理页设置检查位，
因为 [RMP](@amd_rmp) 能保障 VM 仅能写自己的页，
确保了同一时刻一个 guest 的页仅能映射到一个物理页。

如果恶意 hypervisor 通过伪造 [NPT](@term_amd_npt) 换掉了物理页，
新的物理页在 RMP 里肯定没有被设置检查位，从而会被察觉并抛出异常。

![check](https://s3.laisky.com/uploads/2022/09/amd-snp-check.png)

### AMD SEV TEK

AMD SEV Transport Encryption Key

### AMD SEV TIK

AMD SEV Transport Integrity Key

### AMD SEV VCEK

(amd_vcek)=

AMD SEV Versioned Chip Endorsement Key

由硬件私钥 [CEK](@amd_cek) 为某一 TCB 版本派生的 ECDSA 固件私钥。

用于为 SNP REPORT 签名，可表明当前 TCB 版本。

VCEK 的公钥可在 AMD 官网 `https://kdsintf.amd.com` 下载

![vcek-certs](https://s3.laisky.com/uploads/2022/10/amd-vcek-certs.png)

### AMD SEV VEK

AMD SEV VM Encryption Key

为 [CVM](@cvm) 内存加密的 AES 密钥。

### AMD SEV VMPCK

(amd_sev_vmpck)=

AMD SEC VM Platform Communication Keys

CVM 启动时，[SP](@amd_sp) 会向 CVM 的一个特殊的 secrets page 注入四个密钥，
这些密钥将会用于让 CVM 和 SP 间通过 `SNP_GUST_REQUEST` 命令建立加密通讯，使用 `AES-256 GCM` 加密算法。

### AMD SEV VMPLs

(amd_sev_vmpls)=

AMD SEV Virtual Machine Privilege Levels

AMD SEV-SNP 中提供的新功能，本质上就是 [HPD](@term_hpd) 的虚拟化，
为 VM 提供 0~3 四级保护域。

![vmpls](https://s3.laisky.com/uploads/2022/10/amd-vmpls.png)

### AMD SME

(term_amd_sme)=

AMD Secure Memory Encryption

- [CPU Architectures » x86-specific Documentation » 17. AMD Memory Encryption](https://www.kernel.org/doc/html/latest/x86/amd-memory-encryption.html)
- [对抗内存物理读取攻击的利器：Intel TME 和 AMD SME](https://zhuanlan.zhihu.com/p/429055957)

使用一个全局唯一的通用密钥来加密系统内存。该密钥由 AMD 安全处理器在启动时生成。
内存加密对于普通的程序是透明的，仅存在于主存和 CPU 之间，主存内保存密文，CPU 内执行明文。

![sme-flow](https://s3.laisky.com/uploads/2022/09/amd-sme-flow.png)

SME 的 AES 引擎使用的加密密钥是在每次系统重置时随机生成的，并且对软件不可见。密钥由集成在 AMD SOC 上的微控制器 AMD-SP 进行管理。密钥是由板载的符合 SP 800-90 的硬件随机数生成器生成，并存储在专用的硬件寄存器中，永远不会暴露在 SOC 之外。

启动内存加密后，物理地址的第 47 位（又名 `C-bit`，C 代表 enCrypted）用于标记该页是否被加密，对加密页进行访问时，加密和解密将由 AES 引擎自动完成。

![cbit](https://s3.laisky.com/uploads/2022/09/amd-sme-cbit.png)

BIOS 中默认关闭 SME。

对标 [Intel TME](@term_intel_tme)

### AMD SP

(amd_sp)=

AMD Secure Processor

见 [AMD PSP](@psp)

### AMD SVM

(amd-svm)=

AMD Secure Virtual Machine

也称为 SeucreVM。

对标 [Intel TXT](@intel-txt) 的技术。

### AMD TMZ

(amd_tmz)=

AMD Trusted Memory Zone

- [Secure Buffer Support with Trusted Memory Zone.pdf](https://1drv.ms/b/s!Au45o0W1gVVLutRd6UoRDkH_IobO5A?e=bBVWIv)

AMD 推出的 GPU 显存加密技术，让所有显存通过固件 AES 加密。

[Read More...](@page_amd_tmz)

### AMD-V

(term_amd_v)=

- [AMD-V_for_Hackers.pdf](https://1drv.ms/b/s!Au45o0W1gVVLusNh7qgmJybjcxkzcw?e=sfaGc0)

AMD 虚拟化，AMD Virtualization

x86 硬件支持 [VMM](@term_vmm) 对 Ring0 的虚拟化操作。
对标 [Intel VMX](@term_vmx)。

包含：

- [RVI](@term_amd_rvi)
- [NPT](term_amd_npt)

### AMD VCN

(amd_vcn)=

AMD Video Codec Next

### AMD VMCB

(amd_vmcb)=

虚拟机控制块，Virtual Machine Control Block

用户设置和恢复虚拟机进程状态的数据结构，
等同于 [Intel VMCS](@term_intel_vmcs)。

### ARB

Anti-Rollback

防降级攻击

### ARM CCA

(term_arm_cca)=

Arm Confidential Compute Architecture

- <https://www.arm.com/architecture/security-features/arm-confidential-compute-architecture>

![arm-cca](https://s3.laisky.com/uploads/2022/08/arm-cca-software-arch.png)

### ARM Realm

(arm_realm)=

ARM 的 [CVM](@cvm) 方案

### ARM RME

(term_arm_rme)=

ARM Realm Management Extension

- [TrustedFirmware: RME](https://trustedfirmware-a.readthedocs.io/en/latest/components/realm-management-extension.html)

ARM 的隐私计算解决方案，属于 [ARM CCA](@term_arm_cca)。
对标 [Intel SGX](@intel_sgx)。

### ARM TrustZone

(arm-trustzone)=

ARM 的 [TEE](@tee) 技术

![tz](https://s3.laisky.com/uploads/2022/05/arm-trustzone.png)

由三个主要部分构成：

- [AMBA](@arm-trustzone-amba)
- SoC Core
- Debug Infrastrature

### ARM TrustZone AMBA

(arm-trustzone-amba)=

ARM TrustZone Advanced Microcontroller Bus Architecture

### ARM TrustZone NS

(arm-trustzone-ns)=

ARM TrustZone Non-Secure Bit

### ARM TrustZone NSC

(arm-trustzone-nsc)=

ARM TrustZone None Secure Callable

在非安全世界提供了一组进入安全世界的固定入口实现了从非安全世界进入安全世界的通道。
NSC 内可以通过 [SG](@arm_tz_sg) 指令进入安全世界。

NSC 区域用于从非安全世界进入安全世界，这部分的代码能够被非安全世界调用但要遵循一定的规则。
NSC 区域由 `SAU（Security Attribution Unit）`或 `IDAU（Implementation Defined Atrtribute Unit）`定义。

### ARM TrustZone NSW

(arm_tz_nsw)=

ARM TrustZone None Secure World

ARM TrustZone 的非安全世界，用于运行普通的代码，和 [SW](@arm_tz_sw) 相对。

### ARM TrustZone REE

Rich Execution Environment

Arm 的 TrustZone 设计中，在硬件上新增了一个更高的运行级别，称为 Secure World，用于运行安全的代码，而原来的运行级别称为 Non-Secure World，用于运行普通的代码。Secure World 和 Non-Secure World 之间的通信通过 TrustZone 的硬件机制进行隔离，Secure World 中的代码无法访问 Non-Secure World 中的内存，反之亦然。Secure World 中的代码可以访问 Non-Secure World 中的内存，但是需要通过 TrustZone 的硬件机制进行访问，这样就可以保证 Secure World 中的代码无法直接访问 Non-Secure World 中的内存。

Non-Secure 内核称为 REE，Secure 内核称为 TEE。

![ree](https://s3.laisky.com/uploads/2023/05/arm-ree.png)

### ARM TrustZone SCR

(arm_tz_scr)=

ARM TrustZone Secure Configuration Register

SCR 的第 33 位（NS Bit）用于表示 CPU 当前所处的状态

### ARM TrustZone SG

(arm_tz_sg)=

ARM TrustZone Secure Gateway

### ARM TrustZone SMC

(arm_tz_smc)=

Secure Monitor Call

非安全世界向安全世界发起的系统调用。

### ARM TrustZone SW

(arm_tz_sw)=

ARM TrustZone Secure World

ARM TrustZone 的安全世界，用于运行安全代码。和 [NSW](@arm_tz_nsw) 相对。

### ASA

(asa)=

Algorithm Substitution Attack

用来伪造加密结果、签名等。

- [Algorithm Substitution Attacks from a Steganographic Perspective.pdf](https://arxiv.org/abs/1708.06199)

### ASIC

(asic)=

专用集成电路 ASIC, Application-Specific Integrated Circuit

为解决特定应用问题而定制设计的集成电路

### ASLR

(aslr)=

Address Space Layout Randomization

内存地址随机化，以提高安全性，防御 [ROP](@rop)。

### aTLS

(atls)=

attested TLS

指在经过 [Remote Attestation](@remote-attestation) 后，建立可信的 TLS 连接。

### ATS

地址转换服务，Address Translation Service

多用于内存 虚拟地址/物理地址 的转换

### AWS ARN

(aws_arn)=

Amazon Resource Name

AWS 对所有资源的唯一 URN。

### AWS Clean Room

- <https://aws.amazon.com/clean-rooms/>

## B

(term_b)=

### BIOS

Basic Input/Output System

### BitLocker FVEK

(bitlocker_fvek)=

Full Volume Encryption Key

BitLocker 实际加密磁盘所使用的 AES 密钥，会被 [VMK](@bitlocker_vmk) 加密。

![](https://s3.laisky.com/uploads/2023/12/FuhVDwHaIAAfNtO.jpeg)

### BitLocker VMK

(bitlocker_vmk)=

用来加密 FVEK 的 AES 密钥，会被 [TPM](@tpm) sealing 加密。

### BTB

(btb)=

Branch Target Buffers

CPU 用于分支预测的缓存

![btb](https://s3.laisky.com/uploads/2022/10/btb.gif)

### BTI

Branch Target Identification

## C

(term_c)=

### CA

(term_ca)=

Certificate Authority

负责签发证书的权威机构。

每一个 CA 都有一个由上游 CA 签发的证书，
证书中包含 `CA=true` 字段。

若一个 CA 没有上游（证书有自己签发），则称为 `rootCA`。

一些第三方的权威 rootCA 证书会内置在操作系统中，称为`根证书`。
用户通过根证书所建立的信任链，可以校验派生出的中间 CA 和叶子证书。

为了防止 CA 作恶，可以采用第三方的 [CT](@term_ct) 进行记录和监督。

### CASB

Cloud Access Security Broker

> According to Gartner, a cloud access security broker (CASB) is an on-premises or cloud-based security policy enforcement point that is placed between cloud service consumers and cloud service providers to combine and interject enterprise security policies as cloud-based resources are accessed.

可以理解为云时代的跳板机，负责审计和转发客户和云服务商之间的数据。

### CC

歧义：

- [Common Criteria](@common_criteria)
- [Confidential Computing](@term_cc)

#### Common Criteria for Information Technology Security Evaluation

(common_criteria)=

- <https://www.commoncriteriaportal.org/cc/>

信息技术安全评估共同准则，简称共同准则（Common Criteria）或 CC，是针对计算机安全认证的国际标准（ISO/IEC 15408）。
目前的版本是 3.1 版，第 5 次修订。

这是一种静态安全（static trust）评估标准，评估级别分为 `EAL1`~`EAL7`。

#### Confidential Computing

(term_cc)=

机密计算, Confidential Computing

通过构筑 [TEE](@tee) 来实现对数据全方位的防护，主流方案包括：

- [AMD SME](@term_amd_sme)
- [AMD SEV](@amd-sev)
- [Intel SGX](@intel_sgx)
- [Intel MKTME](@intel_mktme)
- [Intel TME](@term_intel_tme)
- [NVIDIA Confidential Computing（H100）](@nvidia_cc)
- [IBM PEF](@ibm_pef)

### CCC

(ccc)=

加密计算协会，Confidential Computing Consortium

Linux Foundation 旗下的，致力于统合软硬件实现 [TEE](@tee) 的非营利性组织。

- <https://confidentialcomputing.io/>
- [CCC Blog](https://confidentialcomputing.io/blog/)

### CCF

Microsoft Confidential Consortium Framework

微软基于 SGX 搞的智能合约框架，底层基于名为 Ledger 的仿 Raft 分布式一致性副本集。

### CDSS

(cdss)=

临床决策支持系统，Clinical Decision Support System

### CFI

(term_cfi)=

控制流完整性，Control Flow Integrity

- [Control-Flow Integrity Principles, Implementations, and Applications.pdf](https://1drv.ms/b/s!Au45o0W1gVVLurkivesS5686jxEXWQ?e=oGhdlz)
- [控制流完整性的发展历程.pdf](https://1drv.ms/b/s!Au45o0W1gVVLurkjhC4FhmZ8ZOxOug?e=348A8K)

一种防御[代码重用攻击](@cra)的方法。

其核心思想是限制程序运行中的控制转移，使之始终处于原有的控制流图所限定的范围内。
具体做法是通过分析程序的控制流图，获取间接转移指令（包括间接跳转、间接调用、和函数返回指令）目标的白名单，
并在运行过程中，核对间接转移指令的目标是否在白名单中。

### CIA

歧义：

- [CIA Triad](@cia_triad)
- [Central Intelligence Agency](@cia)

#### Central Intelligence Agency

(cia)=

美国中央情报局

#### CIA Triad

(cia_triad)=

Confidentiality, Integrity and Availability

![](https://s3.laisky.com/uploads/2023/02/cia_triad.png)

衡量系统安全性的三个视角，一般来说 Integrity 是必须，设计时需要在机密性和可用性间进行权衡。

### CIEM

(ciem)=

Cloud Infrastructure Entitlement Management

在云上践行最小特权原则（the principle of least privilege），
动态管理所有用户和资源的权限。

### CISA

(gov_cisa)=

网络安全与基础设施安全局, Cybersecurity and Infrastructure Security Agency

- <https://github.com/cisagov>
- <https://www.cisa.gov/>

### CoCo

(coco)=

Confidential Container

机密容器，指以云原生的方式，实现机密计算的容器。
常见做法是 kata + SGX/SEV。

### CoT

(cot)=

Chain of Thought

在 ChatAI Prompt Engineering 中的概念，让 AI 不仅仅给出答复，
还要解释其推理过程。

### CPL

(term_cpl)=

当前级别，Current Privilege Level

见 [HPD](@term_hpd)，比如：

- 内核态也称为 `CPL - 0`
- 用户态也称为 `CPL - 3`

### CRA

(cra)=

代码重用攻击，Code-Reuse Attack

利用已有的代码，通过各种跳转手段进行执行，以实现攻击者的目的

包括：

- [JOP](@jop)
- [ROP](@rop)
- JIT spraying

### CRI

(term_cri)=

Kubernetes Container Runtime Interface

类似于 [OCI specification](@term_oci)，不过是由 Kubernetes 主导的容器运行时标准接口。

[OCI](@term_oci) 制定的是在宿主机上运行的标准容器运行时命令行接口，
而 CRI 则是一系列 GRPC API。

### CRI-O

(term_crio)=

CRI-O is an implementation of the CRI to enable using OCI compatible runtimes.

### CRL

(term_crl)=

证书吊销列表 Certificate Revocation List

der 格式的二进制文件，内含一份被吊销的 x509 证书序列号列表。

一般以 `CRL URI` 的形式发布于证书中，tester 可以用这个地址下载 CRL 文件进行比对验证。

### CSP

(term_csp)=

云服务提供商 Cloud Service Providers

在 [SGX](@intel_sgx) [DCAP](@intel-sgx-dcap) 语境中，指那些提供可信计算云服务（包括第三方[远程认证](@intel_sgx_remote_attestation)服务）

### CSPM

(cspm)=

Cloud Security Posture Management

- [What Is CSPM? - Palo Alto Networks](https://laisky.notion.site/What-Is-CSPM-Palo-Alto-Networks-bb9b5d66e9bc456485cc0a14b807f87f?pvs=4)

CSPM 可以理解为中心化的管理中枢，监控所有的其他组件。

### CSR

(term_csr)=

证书签名申请, Certificate Signing Request

当某人希望获得一个证书时，无论是想要获得一个中间 CA 证书，还是一个叶子证书，
都需要用自己的私钥签发一个 CSR，然后交给某个 [CA](@term_ca) 进行签发。

CA 签发 CSR 后会生成一个证书，CA 的签发行为也表示该 CA 愿意为这个新证书背书。

### CSRF

(csrf)=

Cross Site Request Forgery

跨站请求伪造，一种常见的攻击手段。

后端的 Web API 是希望用户在 Web 上发起的调用，
但是攻击者可以通过伪造跨站请求，使得用户在不知情的情况下发起了请求。

防御手段称为 CSRF Token，服务端在返回最初的 Web 页面时会用户设置一个随机 token，
一般可以存放于一个自定义 Header 中。因为 [CORS 请求默认不会允许脚本读取自定义 Header](https://developer.mozilla.org/en-US/docs/Glossary/CORS-safelisted_response_header)。

### CT

歧义：

- [Certificate Transparency](@term_ct)
- [Cipher Text](@ciphertext)

#### Certificate Transparency

(term_ct)=

- <https://www.rfc-editor.org/rfc/rfc6962>
- <https://certificate.transparency.dev/>
- [Certificate Transparency 那些事](https://imququ.com/post/certificate-transparency.html)
- [Certificate Transparency: Go Code](https://github.com/google/certificate-transparency-go)

为防止 [CA](@term_ca) 作恶乱签证书，CT 作为一种补充措施，对所有权威 CA 签发的证书进行记录和跟踪。

#### Cipher Text

(ciphertext)=

有时候会将密文简写为 CT

### CTAP

(ctap)=

Client to Authenticator Protocols

标准时间见 [WebAuthn](@webauthn)。

### CUDA

Compute Unified Device Architecure

Nvidia 推出的针对自家 GPU 的运行时计算框架。

CUDA 运行于用户态，负责与 driver 交互，将用户编写的 CUDA 代码编译为 GPU 指令发送给 driver。

### CUDA SM

(cuda_sm)=

CUDA Streaming Multiprocessor

GPU 计算单元，见[计算模型](@gpu_cuda_compute_model)

### CUDA UVA

(cuda_uva)=

CUDA Unified Virtual Address

本来每个设备的内存都有独立的虚拟地址空间，
通过 CUDA UVA，可以将其组合到同一个虚拟地址空间之中，减少映射转换的开销。

![uva](https://s3.laisky.com/uploads/2022/09/cuda-uva.png)

UVA 的一大优点还在于，解决 [MMIO](@mmio) 难以支持多设备间共享主存地址空间的问题。

[Read More...](@cuda_uva_mem)

### CVM

(cvm)=

加密计算虚拟机, Confidential Virtual Machine

同义词：

- [TVM](@tvm)

方案包括：

- [AMD SEV-SNP](@amd_sev_snp)
- [Intel TDX](@intel-tdx)
- [ARM Realm](@arm_realm)

### CWPP

Cloud Workload Protection Platforms

CWPP 专注于工作节点的防控，一般是 agent 形式。

## D

(term_d)=

### DAA

Direct Anonymous Attestation

### DAC

自主访问控制，Discretionary Access Control

如：

- Linux UGO
- ACL

### Data Lineage

(data-lineage)=

数据血缘

用于对数据进行溯源，追溯某一模型输出结果的来源和依赖。

### Data Masking

(data-masking)=

数据脱敏

对某些敏感信息通过脱敏规则进行数据的变形，实现敏感隐私数据的可靠保护。

### DCT

(term_dct)=

Docker Content Trust

可以使用公私钥对 docker 镜像进行签名，以保证镜像的可信性。

### DEK

(dek)=

Data Encrypt Key

用于加密数据的密钥，一般用于和 [KMS](@keyms) 中的 [KEK](@kek) 区分。

### DES

离散事件系统，Discrete Event Systems

### DHA

Device Health Attestation

Windows 设备健康检查。对 TPM 等设备进行检查。

### Differential Privacy

(differential-privacy)=

差分隐私

- [Wikipedia 差分隐私](https://zh.wikipedia.org/wiki/%E5%B7%AE%E5%88%86%E9%9A%90%E7%A7%81#:~:text=%E5%B7%AE%E5%88%86%E9%9A%90%E7%A7%81%EF%BC%88%E8%8B%B1%E8%AA%9E%EF%BC%9Adifferential%20privacy,%E8%A2%AB%E7%94%A8%E6%9D%A5%E4%BF%9D%E6%8A%A4%E9%9A%90%E7%A7%81%E3%80%82)
- [差分隐私是如何保护个人隐私的？](https://sspai.com/post/68218)
- [差分隐私（一） Differential Privacy 简介](https://zhuanlan.zhihu.com/p/139114240)

### DIP

按病种分值付费，Diagnosis-Intervention Packet

- [国家医疗保障按病种分值付费（DIP）技术规范.pdf](https://1drv.ms/b/s!Au45o0W1gVVLusIFUFkzDp8CPmczmA?e=nx1iaq)

### DKG

(dkg)=

Distributed Key Generation

分布式密钥生成，和传统 [SSS](@sss) 不同的地方在于，不依赖于一个[可信第三方](@ttp)执行密钥中心化生成和分发，
而是各个参与者通过协商直接生成密钥分片。

### DMA

(dma)=

Direct Memory Access

![dma](https://s3.laisky.com/uploads/2022/09/dma.png)

在 CPU 外负责协助 CPU 进行数据读写的协处理器，
使得 CPU 可以不需要浪费计算周期去等待数据就绪。
主要负责和外设交互，在主存和外设间拷贝内存数据。

### DMTF

(dmtf)=

Distributed Management Task Force

- <https://www.dmtf.org/about>

一个 IT 标准化组织。

### DOS

歧义：

- [Deny of Service](@dos)
- [Disk Operating System](@dos_1)

#### Deny of Service

(dos)=

拒绝服务攻击

攻击者让服务失能，无法在正常运行。

#### Disk Operating System

(dos_1)=

磁盘操作系统，被 [GPT](@gpt) 所取代。

### DRG

疾病诊断相关组，Diagnosis Related Groups

- [国家医疗保障疾病诊断相关分组(CHS-DRG)分组与付费技术规范.pdf](https://1drv.ms/b/s!Au45o0W1gVVLusIEIqyaH28z4-UdcQ?e=jdf9OU)

### DRM

歧义：

- [Digital Rights Management](@drm-1)
- [Direct Rendering Manager](@drm)

#### Direct Rendering Manager

(drm)=

Linux 渲染子程序，基于 [KMS](@kms) 在内核中实现显示渲染。

- [an introduction to linux drm subsystem.pdf](https://1drv.ms/b/s!Au45o0W1gVVLutY_c_3vI0i4nMAyeQ?e=9U1foU)

![drm](https://s3.laisky.com/uploads/2022/09/drm.png)

- [DRM Memory Management](https://docs.kernel.org/gpu/drm-mm.html)
- [GEM v. TTM](https://lwn.net/Articles/283793/)

针对图形所需的大内存吞吐进行性能优化，DRM 提供两种内存管理器：

- [TTM](@ttm)
- [GEM](@drm_gem)

#### Digital Rights Management

(drm-1)=

数字版权保护

### DRTM

Dynamic Root of Trust Measurement

### DSPM

(dspm)=

云上数据安全防护，Data Security Posture Management

## E

(term_e)=

### ECC

(ecc)=

椭圆加密算法 Elliptic-curve cryptography

和 RSA 相比最大的优先就是性能更好，且具有 [PFS](@pfs) 特性。

一种非对称加密算法，
最常见的两种实现为 [ECDSA](@ecdsa) 和 [EdDSA](@eddsa)。

### ECDSA

(ecdsa)=

椭圆曲线数字签名算法 Elliptic Curve Digital Signature Algorithm

EC 指的是 Elliptic Curve，即底层理论以 [ECC](@ecc) 密码学为基础，DSA 指的是数字签名算法。
即 DSA 数字签名流程算法在 [ECC](@ecc) 上的实现。

取代 RSA 的新一代非对称加密算法，最大的优点在于性能更好。

据说比不上 [EdDSA](@eddsa)

### ECF

(term_ecf)=

Exceptional Control Flow

Linux 异常处理流程，分为 4 种：

- `interrupts`: 软/硬 中断，由外设异步发起，CPU 执行完当前指令后，检查中断 PIN 脚若发现其在高电位，就会执行相应的中断处理程序，处理完重入进程后会继续执行下一条指令
- `faults`: 处理完成后，会自动重试当前指令（如 `#PF 页错误`）
- `aborts`: 无需返回
- `traps`: 处理完成后作为当前指令的返回，如 syscall

![interrupt](https://s3.laisky.com/uploads/2022/08/interrupt.png)

`interrupts` 被称为异步（asynchronously），因为它是在指令执行完成后才会调度到异常处理程序，而且返回后会执行下一条指令。其他的异常被称为同步（synchronously），因为其依赖异常处理来完成当前指令的功能，所以也被称为 `faulting instruction`。

### EdDSA

(eddsa)=

Edwards-curve Digital Signature Algorithm

[EdDSA](@eddsa) 是 Schnorr signature 签名算法基于 [ECC](@ecc) 的变种，属于 [ECC](@ecc) 椭圆曲线加密范畴，采用的椭圆曲线类型为 twisted Edwards curves。

[EdDSA](@eddsa) 是一个 scheme，即一种算法思想，并不是某种具体的实现，广泛使用的 具体的实现是 Ed25519。
采用的哈希算法是 SHA-512 (SHA-2) ，椭圆曲线是 Curve25519 曲线。

据说安全性要优于 [ECDSA](@ecdsa)。

### Edgeless

(term_edgeless)=

一家专注于做 Golang SGX CloudNative 解决方案的德国公司。

[Read More...](@page_edgeless)

### eFuse

(term_efuse)=

一次性可编程 ROM，多用于存储密钥、序列号等。

fuse 就是保险丝。

[2004 年 IBM 发明了一种超轻量级保险丝的技术](https://s3.laisky.com/uploads/2022/07/efuse.png)，
可以将其运用于芯片上。
在芯片出厂后，可以通过软件调整电流熔断（blowing）保险丝来实现对硬件的重新编码。

可以这么认为，一片 efuse 区域默认都是 1，通过熔断可以将其中一部分改为 0，
从而实现了编码。这是一种一次性操作，不可逆转。

有时候也称为 HardWare Fuse、HW Fuse。

注意不要和 [内存文件系统 FUSE](@term_fuse) 混淆。

### EIP

(eip)=

Ethereum Improvement Proposal

类似于 Pyhton 的 PIP，用于提出 Ethereum 的改进方案。

### ELF

(term_elf)=

Extensible Linked Format

Unix 上广泛使用的可执行文件格式

### Envelope Encryption

(envelope_encryption)=

当采用不复用密钥的情况时，一种减少 KMS 调用频率的策略。

假设对每一个 data 都使用唯一的 data key 进行加密，传统做法是每次都调用 KMS 派生一个新 key 和 keyID。
但是考虑到云上环境，KMS 的调用可能会很贵或者很慢。

为了降低 KMS 的调用频率，提高速度，引入一个 local key。
本地调用 KMS 生成一个 local key 和 local key id，然后本地基于 local key 派生 data key。
这样会牺牲一定的安全性（如果本地缺乏 in-use 的内存防护），但是能极大提高性能。

## F

(term_f)=

### FDE

(fde)=

全盘加密，Full Disk Encryption

### FEC

(term_fec)=

前向纠错码, Forward Error Correction

### FFI

(term_ffi)=

Foreign Function Interface

### FHE

(fhe)=

全同态加密, Full Homomorphic Encryption

### FIDO

线上快速身份认证联盟 Fast Identity Online

- <https://fidoalliance.org/what-is-fido/>

FIDO2 Alliance 包括：

- [U2F](@u2f)
- [UAF](@uaf)
- [CTAP](@ctap)/[WebAuthn](@webauthn)

[Read More...](@fido_desc)

### FIPS

Federal Information Processing Standards

由 [NIST](@nist) 发布的民用数据处理标准。

- [Federal Information Processing Standards](https://en.wikipedia.org/wiki/Federal_Information_Processing_Standards)

### Firmware

固件，由非 CPU 的硬件协处理器运行的软件。

和驱动的区别在于，驱动是由 OS 运行来操作硬件的。

### FL

(term_fl)=

联邦学习，Federated Learning

在多个擁有本地数据样本的分散式边缘设备或服务器上训练算法，再将小模型上传到中心服务器进行整合。
和传统方式的最大区别在于，用户不再上传原始数据，而仅仅上传训练结果。

### FMSPC

(term_fmspc)=

Family-Model-SteppingPlatformCustomSKU

> Description of the processor package or platform instance including its Family, Model, Stepping, Platform Type, and Customized SKU (if applies).

- [Intel® SGX PCK Certificate and Certificate Revocation List Profile Specification.pdf](https://1drv.ms/b/s!Au45o0W1gVVLuqFc8LJK6P4rBcVJ8g?e=VCvagT)

### FPU

(fpu)=

Floating-Point Unit

见 [Register](@term_register)

### FQDN

Fully Qualified Domain Name

域名的完整标识

![FQDN](https://s3.laisky.com/uploads/2022/09/fqdn-01-1024x423.png)

### FUSE

(term_fuse)=

用户态文件系统，Filesystem in USEerspace

## G

(term_g)=

### GC

(gc)=

混淆电路，Garbled Circuit

通过加密门电路的方式完成隐私计算

### GDPR

(gdpr)=

欧盟数据安全法，General Data Protection Regulation

类似的数据安全法规还有：

- Health Insurance Portability and Accountability Act (HIPAA)
- Gramm-Leach-Bliley Act (GLBA)
- the Payment Card Industry Data Security Standard ([PCI DSS](@pci_dss))
- California Consumer Privacy Act (CCPA)

### GDT

(term_gdt)=

Global Descriptor Table

- [The GDT and IDT](http://www.jamesmolloy.co.uk/tutorial_html/4.-The%20GDT%20and%20IDT.html)

在内存还在使用[分段制](@term_mem_segment)的时代，为了寻址，
CPU 需要通过 GDT 来保存所有的段信息。

每个 CPU 都有一个 GDT，该数据结构存储在内存中，头指针地址存储在[寄存器](@term_register) GDT 中。

主要内容包括：

- [段](@term_mem_segment)表
- [TSS](@term_task_state_segment)
- [Thead Local Storage](@term_thread_local_storage)

### GEM

(drm_gem)=

Graphics Execution Manager

[DRM](@drm) 的内存管理工具，比 [TTM](@ttm) 更简单，但是仅支持 [UMA](@uma)。

### GPA

(term_gpa)=

虚拟机物理地址空间，Guset Physical Address

### GPGPU

(gpgpu)=

通用 GPU，Gernal Prupose GPU

### GPR

(gpr)=

Gernal Purpose Registers

见 [Register](@term_register)

### GPT

(gpt)=

GUID Partition Table

GUID 分区表，是一种支持更大磁盘空间、更多分区的新一代磁盘分区表，用于替代 [MBR](@mbr)/[DOS](dos_1)。

### GPU

(gpu)=

图形处理器，Graphics Processing Units

### GPU BO

(gpu_bo)=

GPU Buffer Object

GPU 内存分配的最小单位，每个 BO 由若干个 [PTEs](@term_ptes) 组成

### GPU GART

(term_gart)=

Graphic Address Remapping Tabel

GPU 用于索引 [GTT](@term_gtt) 的信息表。

### GPU GTT

(term_gtt)=

Graphics Translation Table

GPU 想要访问主存时，CPU 为其分配的虚拟地址到物理地址的映射表。

同义词：

- Graphics Aperture Remapping Table
- Graphics Address Remapping Table

GTT 是按需分配的，所以可能在主存内会有多块 GTT，
这些 GTT 的索引信息会保存到 [GART](@term_gart)

### GPU Passthrough

GPU 虚拟化技术，使得 VM 可以使用 GPU 的全部功能。
表现形式就像是把整个 GPU 完全挂载到了 VM 上，宿主机将无法再使用这张显卡。

目前 [CSP](@term_csp) 上更常用的做法是显卡虚拟化（如 [MIG](@nvidia_mig)）。

### GPU SMEM

GPU Shared Memory

### GPU vRAM

(vram)=

GPU 显存，video RAM

### Gramine

(term_gramine)=

一种基于 [SGX](@intel_sgx) 的 [LibOS](@term_libos) 实现。
可以将程序封装进 Enclave 中运行。

曾用名 [Graphene](@term_graphene)

[Read More...](@page_gramine)

### Graphene

(term_graphene)=

SGX LibOS，改名为 [Gramine](@term_gramine)

### GVA

(term_gva)=

虚拟机虚拟地址空间，Guset Virtual Address

### gVisor

(term_gvisor)=

Google 用 Go 语言开发的 [LibOS](@term_libos)，已经被运用于 AppEngine。

[Read More...](@page_gvisor)

## H

(term_h)=

### HDCP

(term_hdcp)=

High-Bandwidth Digital Content Protection

- <https://en.wikipedia.org/wiki/High-bandwidth_Digital_Content_Protection>

为图像设备内置一组密钥，当影像内容在两个图像设备间传输时，
首先协商密钥再加密传输，防止数据内容被中间设备拦截。

### HE

(he)=

同态加密，Homomorphic Encryption

- <https://www.zhihu.com/question/27645858>
- <https://www.zhihu.com/question/27645858/answer/2646273987>

允许人们对密文进行特定形式的代数运算得到仍然是加密的结果，将其解密所得到的结果与对明文进行同样的运算结果一样。 换言之，这项技术令人们可以在加密的数据中进行诸如检索、比较等操作，得出正确的结果，而在整个处理过程中无需对数据进行解密。

可分为：

- [半同态 PHE](@phe)
- [全同态 FHE](@fhe)

### HKA

(hka)=

硬件密钥 Hardware-backed Keystore Authenticators

如：

- [Yubikey](@yubikey)

### HKDF

(hkdf)=

基于哈希和盐的密钥衍生算法，Hash base [KDF](@kdf)

给定一个输入的 key 和盐，可以派生出任意多个密钥。
对于相同的 key 和盐，始终会派生出相同的密钥组。

### HMAC

Hash based MAC

基于 Hash 的 [MAC](@msg_mac) 算法

### HPA

歧义:

- [Host Physical Address](@term_host_phy_addr)
- [Horizontal Pod Autoscaling](@term_k8s_hpa)

#### Horizontal Pod Autoscaling

(term_k8s_hpa)=

- [Horizontal Pod Autoscaling](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/)

#### Host Physical Address

(term_host_phy_addr)=

宿主机物理地址空间, Host Physical Address

同义词：

- [PA](@term_pa)
- [SPA](@spa)

### HPD

(term_hpd)=

分级保护域，Hierarchical Protection Domains

![hpd](https://s3.laisky.com/uploads/2022/08/hpd.jpeg)

CPU 指令集提供了 Ring0 ～ 3 四个不同的保护域，每个保护域都有不同的权限。
如 Ring0 可以访问硬件资源。

Unix 使用 Ring0 运行 kernel，使用 Ring3 运行 Application。
也被称为 kernel/user 态。

其他称谓见：

- [CPL](@term_cpl)
- [IOPL](@term_iopl)
- [Protect Rings](@term_protect_rings)

### HSA

(hsa)=

Heterogeneous System Architecture

- <http://hsafoundation.com/>

AMD 为了推广自己的 [APU](@amd_apu) 成立的生态联盟，看上去已经完蛋。

### HSM

(term_hsm)=

硬件安全模块 Hardware Security Module

有时候也被称为：

- PCSM(personal computer security module)
- SAM(secure application module)

### HSM AKBK

(hsm_akbk)=

HSM AWS Key Backup Key

AWS 的 HSM 服务特有的固件密钥，在 aws 在初始化 HSM 服务时注入，和 [EBK](@hsm_ebk) 一起作为派生根。

### HSM CDK

(hsm_cdk)=

HSM Customer Data Key

HSM 为用户派生的 data key，其私钥明文能够离开 HSM。

### HSM DEK

(hsm_dek)=

HSM Derived Encryption Key

HSM 执行数据加密时所派生的 AES key，这个 key 不会离开 HSM，只会外传 key id。

### HSM EBK

(hsm_ebk)=

HSM Ephemeral Backup Key

HSM 用于加密备份数据的 AES 密钥，一般由 MKBK 派生。

### HSM EKT

(hsm_ekt)=

HSM Exported Key Tokens

当 HSM 的数据要备份时，会将所有的 [HBK](@hsm_hbk) 加密后导出。
这些加密后的密文称为 EKT。

### HSM HBK

(hsm_hbk)=

HSM backing Key

泛指由 HSM 生成的密钥

![Architecture](https://s3.laisky.com/uploads/2023/02/CMK-Hierarchy.png)

### HSM MKBK

(hsm_mkbk)=

HSM Manufacturer Key Backup Key

HSM 固件内置的设备 Root Key，不可读取，可用于派生硬件绑定的密钥。

### HTSS

(htss)=

Hierarchical Threshold Signature Scheme

是 [TSS](@term_threshold_signature_scheme) 的增强，
为每一个 share 都赋予 rank，使得 share 之间不再对等，而是有了等级之分。

### HVA

(term_host_virtual_addr)=

宿主机虚拟内存地址, Host Virtual Address

也称为:

- [VA](@term_va)

### HVM

(hvm)=

硬件虚拟化, hardware virtual machine

- <https://en.wikipedia.org/wiki/Hardware-assisted_virtualization>

也被称为:

- hardware-assisted virtualization
- accelerated virtualization
- native virtualization

相关技术有：

- [AMD-V](@term_amd_v)
- [Intel VMX](@term_vmx)

### HW

Hardware

硬件的简写

### HW Exception

- <https://wiki.osdev.org/Exceptions>

通过硬件中断来和 kernel 通信的方式。如 `#PF` 缺页异常。

### HW Fuse

SGX 文档里会提到 RootKey 被存在 HW Fuse 里，实际上都是指 [efuse](@term_efuse)

### Hygon

中科海光 CPU，国产 CPU 和 GPU，本质是 AMD 的换皮。

包含：

- CPU
- DCU（AMD GPU 换皮）
- [CSV](@hygon_csv)
- CSCV

### Hygon CSV

(hygon_csv)=

海光 CPU 安全虚拟化技术，Hygon China Secure Virtualization

- [龙晰社区海光 CSV SIG](https://openanolis.cn/sig/coco/doc/533508829133259244?lang=zh)
- [海光 CSV 机密容器方案介绍.pdf](https://1drv.ms/b/s!Au45o0W1gVVLutRgfKmNX5WRFkfehw?e=bfLHxH)

[AMD SEV](@amd-sev) 的套皮，把加密固件换成了 SM。

### Hygon DCU

(hygon_dcu)=

Hygon Deep Computing Unit，海光的 [GPGPU](@gpgpu)。

### HyperEnclave

(term_hyperenclave)=

蚂蚁和清华大学发布的，基于 [TPM](@tpm) + [AMD SME](@term_amd_sme) 实现的通用型 TEE 平台。

[Read More...](@page_sgx_hyperenclave)

### Hypervisor

(term_hypervisor)=

即 [VMM](@term_vmm)。

- type 1: bare metal，直接在硬件上运行
- type 2: hosted，运行于宿主机 OS 之上

![hyper](https://s3.laisky.com/uploads/2022/08/Hyperviseur.svg.png)

## I

(term_i)=

### IDT

(term_idt)=

中断描述符表，Interrupt descriptor table

- <https://en.wikipedia.org/wiki/Interrupt_descriptor_table>

记录中断号和中断处理程序的关联表。

### IA

成员推理攻击，Inference Attacks

假设模型是一个黑盒，仅允许调用输入然后获取模型运行结果。
该攻击可以验证一个输入是否存在于模型的训练集中。

### IBB

(ibb)=

Initial Boot Block

firmware 中的第一个代码块，是 CPU 通过 reset vector 完成初始化后，
通过 ACM 加载执行的第一段系统代码。

对 IBB 的度量也称为 [CRTM](@tpm-crtm)。

### IBM PEF

(ibm_pef)=

IBM Protected Execution Facility

### ICL

(icl)=

in-contxt learning

指语言大模型（LLM）对 prompt 上下文的表现出的理解力。

### IDE

(ide)=

Integrity and Data Encryption

### IEC

(iec)=

International Electrotechnical Commission

### IERS

(iers)=

International Earth Rotation and Reference Systems Service

负责根据地球自转管理 UTC 时间的机构。

因为地球旋转越来越慢，为了弥补 UTC 和 原子钟间的时差，IERS 每年评估两次，是否要为 UTC 增加一个闰秒（leap second）。

### Initrd

(initrd)=

initial ramdisk

在系统启动时，在内存中运行的文件系统，用于加载 kernel。

### Intel ACM

Intel Authenticated Code Modules

### Intel AEP

(intel-aep)=

Asynchronous Exit Pointer

当因中断导致 [AEX](@intel-sgx-aex) 后，在 [ISR](@isr) 运行结束后，AEP 指向程序内的某个地址，负责恢复。

![interrupt_handling](https://s3.laisky.com/uploads/2022/05/interrupt_handling.png)

### Intel Amber

Intel Project Amber

Intel 基于 [SGX](@intel_sgx) 和 [TDX](@intel-tdx) 的跨云 TEE 解决方案。

[Read More...](@page_intel_amber)

### Intel AMT

Intel® Active Management Technology

- [AMT flaw](https://www.intel.com/content/www/us/en/architecture-and-technology/intel-amt-vulnerability-announcement.html)

### Intel BG

(intel_bg)=

Intel Boot Guard

- [Leaked Intel Boot Guard keys:What happened? How does it affect the software supply chain?](https://www.notion.so/laisky/Leaked-Intel-Boot-Guard-keys-What-happened-How-does-it-affect-the-software-supply-chain-7e1a93e47da24253998167e364aaccf6?pvs=4)

通过 [ACM](@acm) 来确保 CPU 只会加载执行经过认证的微码和固件。

![](https://s3.laisky.com/uploads/2023/04/intel-bg.png)

### Intel CRS

(intel-crs)=

Intel 证书检索服务，Intel Certificate Retrieval Service

为 DCAP/ECDSA 提供的证书检索服务

- [Intel® Software Guard Extensions (Intel® SGX) Data Center Attestation Primitives- ECDSA Quote Library API.pdf](https://1drv.ms/b/s!Au45o0W1gVVLuot13_tTUqc0ls_XoA?e=hFG2ou)

### Intel EPT

(term_intel_ept)=

扩展页表，Extended Page Table

Intel 对 [SLAT](@term_slat) 的实现。
属于 [VMX](@term_vmx) 的一部分，为[虚拟机物理地址（GPA）](@term_gpa)到
[宿主机物理地址（HPA）](@term_host_phy_addr)的转换提供硬件支持。

![ept](https://s3.laisky.com/uploads/2022/08/ept.png)

### Intel ME

(intel_me)=

Intel Management Engine

运行于 [CPL-3](@term_hpd) 的协处理器。

对标 [AMD PSP](@psp)。

### Intel MKTME

(intel_mktme)=

Multi-Key Total Memory Encryption

- [Intel MKTME enabling](https://lwn.net/Articles/787852/)

对 [Intel TME](@term_intel_tme) 的增强，支持 `2^15 - 1` 个密钥。
可实现逐页加密，根据物理内存地址进行加密。

使用了物理内存中的 15 位用作表示 KeyID。

![mktme-keyid](https://s3.laisky.com/uploads/2022/08/mktme-keyid.png)

### Intel MPA

(intel_sgx_mpa)=

Intel 多 CPU 注册工具，Multi-[Package](@term_package) Registration Agent

[Read More...](@intel_sgx_mpa_install)

### Intel MPX

(term_intel_mpx)=

Intel Memory Protection eXtensions

- [Intel® Memory Protection Extensions Enabling Guide.pdf](https://1drv.ms/b/s!Au45o0W1gVVLurkfYi_k_KeKMfwHjw?e=jlbaTf)
- [Intel® Memory Protection Extensions (Intel® MPX) support in the GCC compiler](http://gcc.gnu.org/wiki/Intel%20MPX%20support%20in%20the%20GCC%20compiler)

Intel 在增加了 4 个 128 位的寄存器 `bnd0 - bnd3`。
每个寄存器可以存一对 64 位的地址边界，交由 GCC 等编译器用来检验指针边界。

![mpx-reg](https://s3.laisky.com/uploads/2022/07/mpx.png)

### Intel IPE

(term_intel_ipe)=

Intel Initial Platform Establishment

硬件组装完成开机后，如果是多 CPU 机器，BIOS 会生成一个 [Platform Key](@intel_platform_key)。

SGX Microcode 还会生成一个 platform manifest，用于 [MPA](@intel_sgx_mpa) 向 [Intel Registration Service](@intel_irs) 注册。

### Intel IPS

(term_intel_ips)=

Intel Provisioning Service

Intel 提供的 [PE](@intel-sgx-pe) 中心验证服务器。

### Intel IRS

(intel_irs)=

Intel Registration Service

Intel 硬件注册中心，响应 [MPA](@intel_sgx_mpa) 发起的注册请求。

### Intel ISM

Intel® Standard Manageability

### Intel IVT

(term_intel_ivt)=

英特尔虚拟化技术，Intel Virtualization Technology

根据具体虚拟化的不同硬件，也被称为:

- [VMX](@term_vmx)
- `VT-i`
- `Vanderpool`
- `VT-x`
- [`VT-d`](@iommu)
- `VT-c`

由英特尔开发的一种虚拟化技术，利用 IVT 可以对在系统上的操作系统，通过[虚拟机查看器 VMM](@term_vmm)，来虚拟一套硬件设备，以供虚拟机操作系统使用。

```sh
➜ cpuid | grep -i "vmx"
      VMX: virtual machine extensions         = true
      VMX: virtual machine extensions         = true
      VMX: virtual machine extensions         = true
      VMX: virtual machine extensions         = true
```

### Intel LFB

(term_lfb)=

Line Fill Buffer

CPU 是乱序执行指令的，为了防止 cache 被锁，所有的 cache miss 都会交给 LFB 去异步执行（加载 or flush）。
所以所有 移入/移出 的缓存理论上都会经过 LFB。

这会成为隐私数据的暴露面，在 [TAA](@intel_taa) 攻击中，LFB 的数据会被嗅探。

### Intel NUC

Intel® Next Unit of Computing

Intel 推出的迷你主机

### Intel PTT

(intel_ptt)=

Intel® Platform Trust Technology

Intel 为低功耗主机设计的兼容 [TPM](@tpm) 2.0 的加密芯片固件。

对标 [AMD fTPM](@amd_ftpm)。

### Intel SBT

Intel® Small Business Technology

### Intel SEAM

(term_seam)=

Intel Secure Arbitration Mode

### Intel SGX

(intel_sgx)=

Software Guard eXtensions

Intel 为第六代 CPU 定义了一组新的指令集，让进程可以创建名为 [enclave](@intel_sgx_enclave) 的地址空间，该地址空间的内存具有进程独占的安全性和完整性保证，不会受到其他特权进程的攻击和窥探。

[More...](@page_sgx_concept)

### Intel SGX AE

(intel-sgx-ae)=

[Intel SGX](@intel_sgx) Architectural Enclaves

Intel 内置的一组系统 enclaves，提供一系列基础功能，包含：

- [PE, Provisioning Enclave](@intel-sgx-pe)
- [LE, Launch Enclave](@intel-sgx-le)
- [QE, Quoting Enclave](@intel_sgx_qe)
- [PCE, Provisioning Certification Enclave](@intel-sgx-pce)
- [PSE, Platform Service Enclaves](@intel-sgx-pse)

### Intel SGX AESM

(intel_sgx_aesm)=

Architectural Enclave Service Manager

- [Communication between Architectural and Application Enclaves](https://sgx101.gitbook.io/sgx101/sgx-bootstrap/enclave/interaction-between-pse-and-application-enclaves)

负责 Application Enclaves 和 [AE](@intel-sgx-ae) 间的通讯。

![aesm](https://s3.laisky.com/uploads/2022/05/ae.png)

其中 Architectural Enclave Service Manager Daemon(aesmd) 负责运行所有的 enclaves。
可以通过 Unix socket `/var/run/aesmd/aesm.sock` 访问 daemon。

```sh
sudo systemctl status aesmd
```

一些 [BUG](@bug_sgx_aesmd) 可能会与 AESMD 没有正常运行有关。

### Intel SGX AEX

(intel-sgx-aex)=

Asynchronous Enclave eXit

enclave 运行时遇到 OS 抛出的异步 [exception](@term_ecf)，需要切换到异常处理程序。
为防止隐私数据泄漏，会启动 AEX 流程。

[Read More...](@sgx_exception)

### Intel SGX AK

(intel_sgx_ak)=

[Intel SGX](@intel_sgx) Attestation Keys

[QE](@intel_sgx_qe) 用来对 [QUOTE](@intel_sgx_quote) 签名的非对称密钥。

AK 由 SGX 硬件的 RK 派生而来。用于签发 QUOTE 进行本地认证。
远程认证时需要用 [PCK](@intel_sgx_pck) 加密。

### Intel SGX Attestation

(intel_sgx_attestation)=

一种证明 [enclave](@intel_sgx_enclave) 可信的机制。enclave 需要向外界证明其确实运行在可信的 [SGX](@intel_sgx) 硬件上。

这一认证的使用场景一般是外部向 [enclave](@intel_sgx_enclave) 发送隐私信息前，
需要 [enclave](@intel_sgx_enclave) 能够证明自己确实可信。

[enclave](@intel_sgx_enclave) 搜集运行证据后，发送给认证方。
根据认证接方的不同，可以分为：

- [本地认证](@intel-sgx-local-attestation)
- [远程认证](@intel_sgx_remote_attestation)

### Intel SGX DCAP

(intel-sgx-dcap)=

[Intel SGX](@intel_sgx) Data Center Attestation Primitives

intel 提供的一系列软件基础设施，用来实现基于 [ECDSA](@ecdsa)/[PCS](@intel_sgx_pcs) 的[远程认证](@intel_sgx_remote_attestation)。

[More...](@page_sgx_concept_dcap)

### Intel SGX ECALLs

(intel-sgx-ecalls)=

Enclave Calls / Enclave Interface Functions

外部程序可以调用 [enclave](@intel_sgx_enclave) 的预定义接口，通过入参和共享内存传递数据，进入 enclave 内运行。

### Intel SGX EDMM

(intel-sgx-edmm)=

[Intel SGX](@intel_sgx) Enclave Dynamic Memory Management

- [SGX EDMM Linux Driver Interface Design](https://github.com/intel/sgx-emm/blob/8d4cb8c6942b63618eedac44e25e2f319e08ac38/design_docs/SGX_EDMM_driver_interface.md)

允许动态扩充 [enclave](@intel_sgx_enclave) 内存空间，解决了 SGX1 里 [enclave](@intel_sgx_enclave) 内存太小的问题。

### Intel SGX EINIT

(intel-sgx-einit)=

Initialize an Enclave for Execution

- [EINIT — Initialize an Enclave for Execution](https://www.felixcloutier.com/x86/einit)

启动 [enclave](@intel_sgx_enclave) 的最后一条指令。
该指令执行完毕后，就可以通过 `EENTER` 指令运行用户代码。

### Intel SGX ELRANGE

(term_intel_sgx_elrange)=

[Enclave](@intel_sgx_enclave) 虚拟内存空间，Intel SGX Enclave Linear Address Range

[tRTS](@term_intel_sgx_trts) 的 Enclave 共享 [uRTS](@term_intel_sgx_urts) 的 Application 进程的整个虚拟地址空间。
但是 enclave 会从中占据一部分空间，映射到 [EPC](@term_intel_sgx_epc) 中作为加密的 enclave 内存空间。

![elrange](https://s3.laisky.com/uploads/2022/08/ELRANGE.png)

在 [SECS](@term_intel_sgx_secs) 中，通过 `BASEADDR` 和 `SIZE` 字段来划定这块内存空间。这块空间的大小应该是 2 的幂次方。

### Intel SGX EMA

[Enclave](@intel_sgx_enclave) 虚拟内存区域，Intel SGX Enclave Memory Area

[EMM](@intel_sgx_emm) 内用来记录和监控 [ELRANGE](@term_intel_sgx_elrange) 区域的数据结构。

没有被 EMA 记录的 [ELRANGE](@term_intel_sgx_elrange) 区域会被视为 free。

### Intel SGX EMM

(intel_sgx_emm)=

[Enclave](@intel_sgx_enclave) 内存管理器，Intel SGX Enclave Memory Management

- [SGX Enclave Memory Manager](https://github.com/intel/sgx-emm/blob/8d4cb8c6942b63618eedac44e25e2f319e08ac38/design_docs/SGX_EMM.md)

试图统合 [Intel sgxsdk](@term_intel_sgx_sdk) 和 [MicroSoft OpenEnclave](@term_openenclave) 这些 runtime，抽象出一个统一的接口层。

![emm](https://s3.laisky.com/uploads/2022/08/emm.png)

EMM 和应用一起运行于 [Enclave](@intel_sgx_enclave) 内部，负责内存分配等一系列基础操作。

### Intel SGX Enclave

(intel_sgx_enclave)=

[SGX](@intel_sgx) 抽象出的容器线程

[Enclave](@intel_sgx_enclave) 内为可信执行环境。enclave 外部无法访问内部的内存。

[More...](@concepts-enclave)

### Intel SGX EPC

(term_intel_sgx_epc)=

Enclave Page Cache

系统中一块被保护的物理内存区域，大小固定，由 BIOS 指定，给 [SGX](@intel_sgx) 使用。

有多种实现方式，包括：

1. [Intel PRM](@intel-sgx-prm)

![prm](https://s3.laisky.com/uploads/2022/08/enclave-prm.png)

EPC 分割为多个 4KB 大小的页，类似于普通内存页的组织方式，可以分配给多个 [enclave](@intel_sgx_enclave) 使用。

![epc](https://s3.laisky.com/uploads/2022/05/epcm.png)

[SGX](@intel_sgx) 可以将内存页（4KB Page）移入或移出 EPC。
当移出 [EPC](@term_intel_sgx_epc) 进入未保护区时，会对其进行加密。
只有当所有 CPU 的缓存都未使用该页时，才能将其移出。

![epc-page](https://s3.laisky.com/uploads/2022/05/epc-page.png)

SGX 将内存换页（swap）的操作交给操作系统，但是因为操作系统并不在 TCB 中，
SGX 会通过 [EPCM](term_intel_sgx_epcm) 来校验对 EPC 页的操作是否合法。

More:

- [SGX Thread](@sgx_thread)

### Intel SGX EPCM

(term_intel_sgx_epcm)=

Enclave Page Cache Map

- <https://sgx101.gitbook.io/sgx101/sgx-bootstrap/enclave#enclave-page-cache-map-epcm>

SGX 扩充了 [PMH](@term_pmh) 的属性，主要包括如下字段：

- `VALID`: 1 bits，标记是否已被分配给 enclave
- `PT`: 9 bits，该页存储的数据类型
- `ENCLAVESECS`: 该页所属的 enclave

上面这些数据可以用来检查操作系统对 [EPC](@term_intel_sgx_epc) 页的分配是否合法。

### Intel SGX EPID

(intel-sgx-epid)=

Enhanced Privacy Identification / Enhanced Privacy Identifier

基于一系列 Intel 的服务（如 [AE](@intel-sgx-ae)），提供 [enclave](@intel_sgx_enclave) 的认证服务。

在 SGX2 中被 [DCAP](@intel-sgx-dcap) 取代。

### Intel SGX FLC

(intel-sgx-flc)=

[Intel SGX](@intel_sgx) Flexible Launch Control

- [Intel(R) SGX Reference Launch Enclave -> Flexible Launch Control](https://github.com/intel/linux-sgx/blob/master/psw/ae/ref_le/ref_le.md#flexible-launch-control)
- [An update on 3rd Party Attestation -> What is Flexible Launch Control?](https://www.intel.com/content/www/us/en/developer/articles/technical/an-update-on-3rd-party-attestation.html)

一种可以改写 [MSR](@term_msrs) 的硬件特性。
通过改写特定寄存器以存入 Launch Control Policy Provider 的 SHA256 签名（[LK](@intel-sgx-lk)）（SIGNING KEY，`MRSIGNER`），
从而实现启动自定义 [LE](@intel-sgx-le)。

要启用 FLC，BIOS 中支持两种设置模式：

1. Unlocked mode：
2. Locked mode：只有 BIOS 可以设置 `IA32_SGXPUBKEYHASH0..3` 的值

### Intel SGX IAS

(intel-sgx-ias)=

Intel Attestation Service

Intel 为 SGX1 设计的为 [EPID](@intel-sgx-epid) 提供认真服务的中心服务器。

### Intel SGX LE

(intel-sgx-le)=

[Intel SGX](@intel_sgx) Launch Enclave

- [Intel(R) SGX Reference Launch Enclave](https://github.com/intel/linux-sgx/blob/master/psw/ae/ref_le/ref_le.md)

[LE](@intel-sgx-le) 作为 [AE](@intel-sgx-ae) 中的一部分，主要职责为：

1. 判断一个 [enclave](@intel_sgx_enclave) 是否允许被启动
2. 为其他 [enclave](@intel_sgx_enclave) 创建 `Launch Token`。

`Launch Token` 会被系统传递给驱动的 [EINIT](@intel-sgx-einit) 流程。

根据整套流程是否由 Intel 签发，可以将 [LE](@intel-sgx-le) 分为：

1. 默认的 [LE](@intel-sgx-le) 仅支持 [Intel 的 PSW](@intel-sgx-psw)
2. `ref-LE` 可以由第三方自行开发

自定义的 `ref-LE` 必须被 Launch Control Policy Provider 签名，
才能被以 [LE](@intel-sgx-le) 的形式启动。

Launch Control Policy Provider 的 SHA256 签名必须存储在 `IA32_SGXPUBKEYHASH0..3` 寄存器中。
而改写 `IA32_SGXPUBKEYHASH0..3` 寄存器就依赖于 [FLC](@intel-sgx-flc) 机制。

SGX LE 取代了 [Intel TXT](@intel-txt) 中的 SINIT ACM。

### Intel SGX LK

(intel-sgx-lk)=

[Intel SGX](@intel_sgx) Launch Key

[LK](@intel-sgx-lk) 由 [RSK](@intel-sgx-rsk) 生成。

SGX1 中，[LE](@intel-sgx-le) 用来生成 `EINITTOKEN` 的私钥。

### Intel SGX Local Attestation

(intel-sgx-local-attestation)=

[SGX](@intel_sgx) [enclave](@intel_sgx_enclave) 本地认证。

[SGX](@intel_sgx) [enclave](@intel_sgx_enclave) 通过 EREPORT hardware instruction 收集 [REPORT](@intel_sgx_report) 后，
发送给本地认证者。

目的：相同机器上的 [enclave](@intel_sgx_enclave) 应用互相认证运行于同一个 SGX 硬件上。（但是并不能确保 SGX 环境是可信的，这需要[远程认证](@intel_sgx_remote_attestation)）。

所有的 [REPORT](@intel_sgx_report) 都通过硬件的 `REPORT MAC` 对称密钥加密，
所以所有同一平台的 [enclave](@intel_sgx_enclave) 都可以认证这份 [REPORT](@intel_sgx_report) 是来自于本地的可信 [SGX](@intel_sgx) 环境。

### Intel SGX OCalls

(term_intel_sgx_ocalls)=

Outside Calls

Enclave 向外部非可信区发起的调用。

### Intel SGX PCCS

(intel-sgx-pccs)=

Provisioning Certification Caching Service

由平台方部署的第三方缓存，用于加速 [SGX](@intel_sgx) 机器和 [PCS](@intel_sgx_pcs) 的通信。

- [Intel® Software Guard Extensions Data Center Attestation Primitives (Intel® SGX DCAP): A Quick Install Guide](https://www.intel.com/content/www/us/en/developer/articles/guide/intel-software-guard-extensions-data-center-attestation-primitives-quick-install-guide.html)
- [Design Guide for Intel® SGX Provisioning Certificate Caching Service (Intel® SGX PCCS).pdf](https://1drv.ms/b/s!Au45o0W1gVVLuopGCdDKGOiqmtDOQg?e=wJsu7g)
- [安装 PCCS](@page_sgx_pccs)

### Intel SGX PCE

(intel-sgx-pce)=

[Intel SGX](@intel_sgx) Provisioning Certification Enclave

> Intel® Software Guard Extensions (Intel® SGX) [enclave](@intel_sgx_enclave) that uses a Provisioning Certification Key to sign proofs that attestation keys or attestation key provisioning protocol messages are created on genuine hardware.

基础 [AE](@intel-sgx-ae) 的一部分。

负责向 [PCS](@intel_sgx_pcs) 请求认证数据（`attestation collateral`）
以启动 [DCAP](@intel-sgx-dcap)。

之后负责使用 [PCK](@intel_sgx_pck) 对 [REPORT](@intel_sgx_report) 进行签名。

一般只在 [SGX](@intel_sgx) 机器初始化时启动一次，之后会定期轮询更新缓存。

为了减少网络延迟，平台方可以部署 [PCS](@intel_sgx_pcs) 的缓存 [PCCS](@intel-sgx-pccs)。

[PCE](@intel-sgx-pce) 也有自己的 [SVN](@intel-sgx-svn)，称为 `PCE SVN`。

### Intel SGX PCK

(intel_sgx_pck)=

Provisioning Certification Key

[PCE](@intel-sgx-pce) 用来签名 [REPORT](@intel_sgx_report) 的密钥。
都派生自 [PCK Cert](@intel_sgx_pck_cert)。

> The key is unique to a processor package or platform instance, the Hardware TCB, and the [PCE](@intel-sgx-pce) version (PSVN).

### Intel SGX PCK Cert

(intel_sgx_pck_cert)=

Provisioning Certification Key Certification

由 Intel 为每一个 [PCE](@intel-sgx-pce) 硬件签发的证书。

公钥发布在公网上，[远程认证](@intel_sgx_remote_attestation)时的
外部认证者（verifier）可以通过证书校验 [QUOTE](@intel_sgx_quote) 的签名。

### Intel SGX PCKIDRetrievalTool

Intel SGX PCK Provisioning tool

[More...](@sgx_pck_provision_tool)

### Intel SGX PCS

(intel_sgx_pcs)=

Intel Provisioning Certification Service

为 SGX2 的 [DCAP](@intel-sgx-dcap) 实现了新的 Intel 认证服务器。

第三方认证服务器（verifier）可以从 Intel [PCS](@intel_sgx_pcs) 获取 PKI 信息。

- [Intel® SGX Services for ECDSA Attestation](https://api.portal.trustedservices.intel.com/)

### Intel SGX PE

(intel-sgx-pe)=

[Intel SGX](@intel_sgx) Provisioning Enclave

有时候也简称为 PvE。

负责基于 [EPID](@intel-sgx-epid) 的[远程认证](@intel_sgx_remote_attestation)。

在 [SGX](@intel_sgx) 机器启动时，PE 会向 [IPC](@term_intel_ips) 服务器发起认证请求。

[PE](@intel-sgx-pe) 最主要的使用者就是 [QE](@intel_sgx_qe)

### Intel SGX PK

歧义：

- [Intel SGX Provisioning Key](@intel-sgx-pk)
- [Intel SGX Platform Key](@intel_platform_key)

#### Intel SGX Provisioning Key

(intel-sgx-pk)=

由 [RPK](@intel-sgx-rpk) 派生而来。
当 [enclave](@intel_sgx_enclave) 和 [IPS](@term_intel_ips) 进行[远程认证](@intel_sgx_remote_attestation)时使用。

[More...](@page_sgx_concept_pk)

#### Intel SGX Platform Key

(intel_platform_key)=

对于 Multi-Package Platform（多 CPU 机器），硬件组装好开机的时候，BIOS 综合所有 CPU Key 生成 platform key。
然后在[远程认证](@intel_sgx_remote_attestation)的时候，通过 `platform key -> provision key -> attestation key` 派生出 [AK](@intel_sgx_ak)。（单 CPU 机器上这一派生流程是 `CPU Hardware Key -> provision key -> attestation key`）。

问题是 Intel 并不知道你的 platform key，因为这个 key 来自于机器组装后，
所以 Intel 没法在[远程认证](@intel_sgx_remote_attestation)时校验 [AK](@intel_sgx_ak)。
就需要你用 [MPA](@intel_sgx_mpa) 把 platform key 注册给 intel

### Intel SGX PRM

(intel-sgx-prm)=

进程专属内存，Process Reserved Memory

划定一块物理内粗区域仅供某一进程使用，拒绝其他一切进程或特权软硬件的访问。

[EPC](@term_intel_sgx_epc) 的一种实现方式，由 BIOS 分配一块物理内存区域，留给 [EPC](@term_intel_sgx_epc) 使用。

### Intel SGX PSE

(intel-sgx-pse)=

[Intel SGX](@intel_sgx) Platform Service Enclaves

为了隔离 [enclave](@intel_sgx_enclave) 和操作系统，为其他 [enclave](@intel_sgx_enclave) 提供一些基础的系统服务，如：

- 单调计数器
- 可信时钟

### Intel SGX PSVN

(intel-sgx-psvn)=

[Intel SGX](@intel_sgx) Platform Security Version Numbers

[SGX](@intel_sgx) [TCB](@tcb) 内的全部 [SVN](@intel-sgx-svn) 信息，包括 [PCE](@intel-sgx-pce) SVN。

### Intel SGX PSW

(intel-sgx-psw)=

[Intel SGX](@intel_sgx) Platform Software

包含所有 [AE](@intel-sgx-ae) 的软件基础设施。

一般指老的（SGX1）基于 [EPID](@intel-sgx-epid)/[IAS](@intel-sgx-ias) 的[远程认证](@intel_sgx_remote_attestation)。

### Intel SGX QE

(intel_sgx_qe)=

[Intel SGX](@intel_sgx) Quoting Enclave

用非对称密钥将 [REPORT](@intel_sgx_report) 签名生成 [QUOTE](@intel_sgx_quote)。

[QE](@intel_sgx_qe) 在有的文档里被称为 [Architecture enclave](@intel-sgx-ae)，
有的地方被称为 Application Enclave。

~~我的理解是，SGX1 时代用 [Intel PK](@intel-sgx-pk) 做远程认证时是 AE。
SGX2 里使用用户自定义 [AK](@intel_sgx_ak) 做认证时就是 Application Enclave。~~

[QE](@intel_sgx_qe) 一般会被包括于 [QPL](@intel_sgx_qpl) 中，
在编译服务端程序的时候打包编译和发布。

### Intel SGX QPL

(intel_sgx_qpl)=

[Intel SGX](@intel_sgx) Quote Provider Library

- [安装 QPL](@page_sgx_sdk_qpl)

内嵌了一个 Intel 签发的 [QE](@intel_sgx_qe) 的库，
可以用来生成 [QUOTE](@intel_sgx_quote)。

在[远程认证](@intel_sgx_remote_attestation)中，待认证的服务端 [enclave](@intel_sgx_enclave) 需要通过调用 QPL/QE 生成一个 Quote。

[QPL](@intel_sgx_qpl) 启动的时候会调用 [PCCS](@intel-sgx-pccs)，[源码](https://github.com/intel/SGXDataCenterAttestationPrimitives/blob/e420ca703fb96330d6e03d5a138aea424b2e8bd1/QuoteGeneration/qcnl/linux/config.cpp#L50)。

### Intel SGX Quote

(intel_sgx_quote)=

attesting [enclave](@intel_sgx_enclave) 生成一个专用的 [SGX Report](@intel_sgx_report)，
然后将 Report 交给 [QE](@intel_sgx_qe) 生成 Quote，
Quote 内会内嵌 Report。

和 [REPORT](@intel_sgx_report) 相比最大的区别就是，
Quote 一般被用于外部第三方的[远程认证](@intel_sgx_remote_attestation)。

### Intel SGX QvE

(intel-sgx-qve)=

[Intel SGX](@intel_sgx) Quote Verification Enclave

和 [QE](@intel_sgx_qe) 的概念相对应，由 Intel 签名的，用于验证 [QUOTE](@intel_sgx_quote) 的 Enclave。

也需要请求 [PCCS](@intel-sgx-pccs) 获取 [PCK Cert](@intel_sgx_pck_cert)。

### Intel SGX QVL

(intel-sgx-qvl)=

[Intel SGX](@intel_sgx) Quote Verification Library

和 [QPL](@intel_sgx_qpl) 的概念相对应，是用于做验证（verification）的库。

### Intel SGX RA

Intel SGX Remote Attestation

(intel_sgx_remote_attestation)=

[SGX](@intel_sgx) [enclave](@intel_sgx_enclave) 远程认证。

- [An update on 3rd Party Attestation](https://www.intel.com/content/www/us/en/developer/articles/technical/an-update-on-3rd-party-attestation.html)

[enclave](@intel_sgx_enclave) 应用将[本地认证](@intel-sgx-local-attestation) 生成的 [REPORT](@intel_sgx_report)，
然后交给 [QE](@intel_sgx_qe) 使用 [AK](@intel_sgx_ak) 签名生成
[QUOTE](@intel_sgx_quote)。用于向客户证明 [enclave 应用](@intel_sgx_enclave)确实运行于合法的 SGX 环境中。

历史变更：

- SGX1 由 Intel 提供：[EPID](@intel-sgx-epid)/[IAS](@intel-sgx-ias)
- SGX2 由 [DCAP](@intel-sgx-dcap) 实现第三方认证

参与者：

- Attester（server）：服务端程序，负责收集平台的证据（[REPORT](@intel_sgx_report)）
- Verifier（client）：负责校验 report，确认服务端确实运行于 [TEE](@tee) 之中

[Read More...](@sgx_concept_ra)

### Intel SGX Report

(intel_sgx_report)=

[SGX](@intel_sgx) 硬件对 [enclave](@intel_sgx_enclave) 进行度量时所生成的数据结构，
用于[本地认证](@intel-sgx-local-attestation)。

在[远程认证](@intel_sgx_remote_attestation) 时，Report 会被内嵌于 [QUOTE](@intel_sgx_quote) 中。

Report 内可以包含最长 64 bytes 的自定义数据。
一般用于存放服务端自签证书的哈希签名，客户端可以用来校验服务端接口证书的合法性。

Report 中保存的值有：

- Data: 用户自定义 64 bytes 的数据
- Security Version(`ISVSVN`): 用户自定义应用版本
- Product ID（`ISVPRODID`）：uint16，用户自定义的产品版本
- Debug: 是否是 DEBUG 模式
- `MRENCLAVE`: 32B，enclave 的 SHA256
- `MRSIGNER`: 公钥的签名
- TCBStatus
  - `UpToDate`
  - `OutOfDate`
  - `Revoked`
  - `ConfigurationNeeded`
  - `OutOfDateConfigurationNeeded`
  - `SWHardeningNeeded`
  - `ConfigurationAndSWHardeningNeeded`
  - `Unknown`

### Intel SGX RPK

(intel-sgx-rpk)=

[Intel SGX](@intel_sgx) Root Provisioning Key

用于做[认证](@intel_sgx_attestation)，Intel 会保存所有出厂的 [RPK](@intel-sgx-rpk) 记录。

可以用来派生 [PK](@intel-sgx-pk)。

[More...](@sgx-concept-rpk)

### Intel SGX RK

(intel-sgx-rk)=

[Intel SGX Report](@intel_sgx_report) Key

由 [RSK](@intel-sgx-rsk) 生成，用于[本地认证](@intel-sgx-local-attestation)。

### Intel SGX RSK

(intel-sgx-rsk)=

[Intel SGX](@intel_sgx) Root Seal Key

出厂预置于硬件中的密钥。
用于做[加密](@intel_sgx_sealing)，Intel 声称会销毁所有的 [RSK](@intel-sgx-rsk) 记录

### Intel SGX Runtime

(term_intel_sgx_runtime)=

SGX 中将运行时分为三个部分：

1. Kernel(Drivers)：特权软件，不可信
2. [uRTS](@term_intel_sgx_urts)：不可信的用户态程序
3. [tRTS](@term_intel_sgx_trts)：可信的 Enclave 应用

![sgx-runtime](https://s3.laisky.com/uploads/2022/08/sgx-trts.png)

### Intel SGX Sealing

(intel_sgx_sealing)=

- [Introduction to Intel® SGX Sealing](https://www.intel.com/content/www/us/en/developer/articles/technical/introduction-to-intel-sgx-sealing.html)
- [Intel SGX Sealing](https://insujang.github.io/2017-10-09/intel-sgx-sealing/#:~:text=Sealing%20is%20a%20service%20that,the%20enclave%20will%20be%20lost.)

[enclave](@intel_sgx_enclave) 退出后会被销毁，如果想要在磁盘持久化加密加密数据，则需要使用到 sealing 机制。

SGX 提供了两组内置的密钥给 enclave 用来加解密：

- Enclave Identity: 具有相同 `MRENCLAVE`（UniqueID） 的 enclave 共享同一个密钥
- Signing Identity: 具有相同 `MRSIGNER`（SignerID） 的 enclave 共享同一个密钥

{{< hint warning >}}
⚠️ 注意：[Sealing Key](@intel_sgx_sk) 是由 CPU 生成的，相同 enclave 在不同机器上会拿到不同的值。
{{< /hint >}}

### Intel SGX SECS

(term_intel_sgx_secs)=

[Intel SGX](@intel_sgx) Enclave Control Structure

[enclave](@intel_sgx_enclave) 内存结构中用于保存元数据的结构。

### Intel SGX SDK

(term_intel_sgx_sdk)=

[Intel SGX](@intel_sgx) Software Development Kit

[SGX](@intel_sgx) SDK 特指由 Intel 提供的一系列开发工具，帮助开发者将 [enclave](@intel_sgx_enclave) 打包为 `.so` 文件，
可供其他普通程序调用。

- [Intel® SGX Software Installation Guide For Linux OS.pdf](https://1drv.ms/b/s!Au45o0W1gVVLuolV8KML22JJWGyVuA?e=uDJGg2)
- [Intel® Software Guard Extensions (Intel® SGX) SDK for Linux OS.pdf](https://1drv.ms/b/s!Au45o0W1gVVLuolUM7hlPGodSXG2lA?e=FcOWMx)

[Read More...](@page_sgx_sdk)

### Intel SGX SK

(intel_sgx_sk)=

[Intel SGX](@intel_sgx) Sealing Key

[Enclave](@intel_sgx_enclave) 调用 SGX 指令由 [RSK](@intel-sgx-rsk) 派生而来。

当 [enclave](@intel_sgx_enclave) 想持久化存储数据时，可以申请 Sealing Key 用于数据加解密。
因为密钥和加解密过程都发生于 [enclave](@intel_sgx_enclave) 的内存空间内，所以最大程度保证了安全性。

更多内容见 [Intel SGX Sealing](@intel_sgx_sealing)

### Intel SGX SSA

(term_intel_sgx_ssa)=

[Intel SGX](@intel_sgx) Save State Area

每个 [enclave TCS](@term_intel_sgx_tcs) 至少有一个 SSA，用来在 [AEX](@intel-sgx-aex) 保存线程寄存器状态。
是属于 SGX Thread Local Storage 的一部分。

### Intel SGX SVN

(intel-sgx-svn)=

[Intel SGX](@intel_sgx) Security Version Number

`EGETKEY` 指令获取 [enclave](@intel_sgx_enclave) 的序列号信息：

- `CPU SVN`：处理器微码版本
- `ISV SVN`：enclave 软件版本

### Intel SGX TCS

(term_intel_sgx_tcs)=

Thread Control Structure

[enclave](@intel_sgx_enclave) 内存数据结构中用于保存 [enclave](@intel_sgx_enclave) 线程上下文切换的信息。
每一个 [enclave](@intel_sgx_enclave) 线程都对应一个 TCS。

TCS 默认栈大小为 4K，最多设置 1024 个 TCS。

[More...](@sgx_thread)

### Intel SGX tRTS

(term_intel_sgx_trts)=

Intel SGX Trusted Run-time System

运行于可信环境中的 encalve 应用，属于 [SGX Runtime](@term_intel_sgx_runtime)。

### Intel SGX uRTS

(term_intel_sgx_urts)=

Intel SGX Untrusted Run-time System

运行于不可信环境中的用户态程序，属于 [SGX Runtime](@term_intel_sgx_runtime)。

### Intel SPS

(intel_sps)=

Intel® Server Platform Services

看上去似乎是替代 [Intel ME](@intel_me)。

### Intel TAA

(intel_taa)=

Intel TSX Asynchronous Abort

- [Intel® Transactional Synchronization Extensions (Intel® TSX) Asynchronous Abort / CVE-2019-11135 / INTEL-SA-00270](https://www.intel.com/content/www/us/en/developer/articles/technical/software-security-guidance/advisory-guidance/intel-tsx-asynchronous-abort.html)
- [Diminisher - A Linux Kernel based Countermeasure for TAA Vulnerability.pdf](https://s3.laisky.com/public/papers/security/TEE/SGX/Diminisher%20-%20A%20Linux%20Kernel%20based%20Countermeasure%20for%20TAA%20Vulnerability.pdf)

TAA 常被攻击者用来嗅探 [LFB](@term_lfb)。

TAA 漏洞的本质就是通过占满缓存，让目标数据被 cache evict，然后通过 TAA 漏洞嗅探 LFB，从而获取隐私数据。

![taa-attack](https://s3.laisky.com/uploads/2022/06/taa-attack.png)

### Intel TD

(intel_td)=

Intel® Trutst Domain

### Intel TDX

(intel-tdx)=

Intel® Trust Domain eXtensions

Intel 的 [CVM](@cvm) 方案。

基于 [Intel MKTME](@intel_mktme) 的 VMM 内存加密技术，为每一个虚拟机都提供独立的内存透明加密密钥。
还支持基于 [Intel SGX](@intel_sgx) 的远程认证。类似于 [AMD SEV](@amd-sev)。

[Read More...](@page_intel_tdx)

### Intel TDX TD

Intel TDX Tust Domains

TDX 中的 confidential VMs。

### Intel TME

(term_intel_tme)=

Intel Total Memory Encryption

对标 [AMD SME](@term_amd_sme)，主存全局加密，CPU 使用内置 AES 密钥进行加解密。

### Intel TXE

Intel Trusted Execution Engine

Intel 的安全协处理器

### Intel TXT

(intel-txt)=

Intel® Trusted eXecution Technology

基于 [TPM](@tpm) PCR，通过一组安全扩展，为系统创建一个被保护的环境。

静态度量部分称为 [LCP](@lcp)，动态度量部分称为 [MLE](@mle)。

在设计时缺乏对 [SMM](@smm) 的考虑导致可被绕过。
[SGX](@intel_sgx) 的硬件保护机制可以防止被 [SMM](@smm) 绕过。

### Intel VMCS

(term_intel_vmcs)=

Intel Virtual Machine Control Structure

Intel 通过 [VMCS](@term_intel_vmcs) 来管理 VMM 中的进程。
分为状态区和控制区，VM 恢复运行时，将状态区的数据覆盖 CPU 上下文，然后根据控制区设置拦截。

在 AMD 的对标称为 [VMCB](@amd_vmcb)

![vmcs](https://s3.laisky.com/uploads/2022/08/intel-vmcs.png)

每个 [Intel VMM](@term_intel_vmm) 都有一到多个 [VMCS](@term_intel_vmcs)。
一般一个 VMCS 对应一个虚拟机内的进程。

每个 CPU 核在同一时间只能运行一个 [VMCS](@term_intel_vmcs)，
通过一个寄存器指向当前运行的 VMCS。

每个 VMCS 有一些重要的属性：

- `Guest State`: 虚拟机内进程的状态
- `Host state`: The state of the processor is loaded from here during a VM exit
- `VM execution control`: 可以设置指令黑白名单，VM 执行不被允许的指令时会触发 VM exit
- `VM enter control`: VM enter 时的控制（从 root 到 nonroot 切换时触发）
- `VM exit control`: VM exit 时的控制（从 nonroot 到 root 切换时触发）
- `VM exit reason`: VM exit 的原因

### Intel VMM

(term_intel_vmm)=

虚拟机管理器，Virtual Machine Monitor

![intel_vmm](https://s3.laisky.com/uploads/2022/08/intel_vmm.png)

_（感觉和[虚拟机管理器 VMM](@term_vmm)没什么区别，就是 Intel 对 [VMM](@term_vmm) 的另一种称呼。）_

### Intel VMX

(term_vmx)=

虚拟机扩展，Virtual Machine eXtensions

也被称为:

- [Intel IVT](@term_intel_ivt)

Relates:

- [Intel VMX technology.pdf](https://1drv.ms/b/s!Au45o0W1gVVLusAPgX2XBfm1Ytufzw?e=iimwQH)
- [对标 AMD-V](@term_amd_v)
- [trap-and-emulate.ppt](https://1drv.ms/b/s!Au45o0W1gVVLuo9vkPkN0rTXkbsvvQ?e=XV3TvF)

Intel x86 硬件支持 [Intel VMM](@term_intel_vmm) 对 Ring0 的虚拟化操作。
硬件虚拟化运行 CPU 在遇到指定指令时执行 `VM EXIT`，
将控制权切换给 VMM，从而得以实现对任意指令的拦截。

为 CPU 新增了两种状态：`root`/`non-root`。
和原有的 `user`/`kernel` 组合后可得四种状态:

- root/user: [Intel VMM](@term_intel_vmm) 运行于用户态
- root/kernel: [Intel VMM](@term_intel_vmm) 运行于内核态
- non-root/user: VM 运行于用户态
- non-root/kernel: VM 运行于内核态（guest OS）

注：VM/guest 指运行于 VMM 内的虚拟操作系统。

Intel 通过 [VMCS](@term_intel_vmcs) 来管理 VMM 中的进程。

### ISA

(isa)=

Industry Standard Architecture

一种古老的 16-bit 总线设备，发源于 8-bit 的 IBM PC bus 和 16-bit 的 IBM AT bus。
也曾试图过度到 32-bit，但是最终被 32-bit PCI 取代。

（感觉 ISA 很多时候被用来指代那些 32-bit 甚至更低的古老设备）

### ISO

(iso)=

International Organization for Standar·dization

国际标准化组织

### IOMMU

(iommu)=

I/O Memory Management Unit

在 Intel 被称为 VT-d，在 AMD 被称为 IOMMU。

功能类似于 [MMU](@mmu)，外部设备想要访问主存时，
需要将外设的虚拟地址映射到物理地址，IOMMU 就扮演地址转换的功能，
并且负责和 [DMA](@dma) 交互获取内存。

![iommu](https://s3.laisky.com/uploads/2022/09/iommu-mmu.png)

### IOPL

(term_iopl)=

IO 权限级别，Input/Output Privilege Level

见[HPD](@term_hpd)。

### ISMS

(isms)=

信息安全管理体系, Information Security Management System

### ISOC

(isoc)=

Information Security Operations Center

是 [SOC](@soc_team) 的同义词

### ISR

(isr)=

中断服务程序, Interrupt Service Routine

当发生某个中断时，负责该中断事件的软件程序。

如 linux 2.6 以前，就是通过触发 `0x80` 来让 ISR 执行 syscall。

### ISV

(term_isv)=

独立软件提供者，Independent Software Vendor

硬件厂商喜欢使用这个词来指代不受他们控制的软件。

比如 [SGX](@intel_sgx) ISV 就是指开发者自己编写的运行于 [SGX Enclave](@intel_sgx_enclave) 内的软件。
[Enclave](@intel_sgx_enclave) 内除了 ISV 外还有 Intel 自己的 [tRTS](@term_intel_sgx_trts)，
使用 ISV 就是为了将开发者自行编写的软件和硬件提供商的硬件做区分。

### IV

(iv)=

Initialization Vector

- <https://en.wikipedia.org/wiki/Initialization_vector>

同义词：[SV](@sv)

## J

(term_j)=

### JOP

(jop)=

Jump-Oriented Programming

[CRA](@cra) 的一种，通过恶意使用 `jump` 来执行代码。

### JTC

(jtc)=

Join Technical Committee

是 [ISO](@iso) 和 [IEC](@iec) 的联合工作组。

## K

(term_k)=

### Kata

(term_kata)=

以轻量级 VM 为容器的 OCI runtime

[Read More...](@page_secure_vm_kata)

### KDF

(kdf)=

密钥衍生算法 Key Derivation Function

通过指定的材料，生成出一个或多个密钥

### KEK

(kek)=

Key Encrypt Key

用于加密密钥的密钥，一般用于和 [KMS](@keyms) 中的 [DEK](@dek) 区分。

### KLOC

每千行代码, thousands(K) of Lines Of Code

### KMS

歧义：

- [Kernel Mode Setting](@kms)
- [Key Management Service](@keyms)

#### Kernel Mode Setting

(kms)=

![kms](https://s3.laisky.com/uploads/2022/09/kms.png)

#### Key Management Service

(keyms)=

密钥管理系统

### KYC

(kyc)=

Know Your Customer, 实名认证

## L

(term_l)=

### LAPIC

(lapic)=

Local Advanced Programmable Interrupt Controller

是一种负责接收 / 发送中断的芯片，集成在 CPU 内部，每个 CPU 有一个属于自己的 LAPIC。它们通过 APIC ID 进行区分。

每个 LAPIC 都有自己的一系列寄存器、一个内部时钟、一个本地定时设备 和 两条 IRQ 线 LINT0 和 LINT1。
LAPIC 寄存器是一段起始地址为 0xFEE00000 、长度为 4KB 的物理地址区域。

常用寄存器：

- ICR(Interrupt Command Register)：用于发送 IPI
- IRR(Interrupt Request Register)：当前 LAPIC 接收到的中断请求
- ISR(In-Service Register)：当前 LAPIC 送入 CPU 中 (CPU 正在处理) 的中断请求
- TPR(Task Priority Register)：当前 CPU 处理中断所需的优先级
- PPR(Processor Priority Register)：当前 CPU 处理中断所需的优先级，只读，由 TPR 决定

### LCP

(lcp)=

Launch Control Policy

### LDT

(term_ldt)=

Local Descriptor Table

- [Wiki](https://en.wikipedia.org/wiki/Global_Descriptor_Table#Local_Descriptor_Table)

一般存放于 [GDT](@term_gdt) 中，用于保存一些进程/线程相关的本地量。

### LibOS

(term_libos)=

Library Operation System

在用户空间实现操作系统的功能

[Read More...](@page_libos)

### Linux EVM

(linux-evm)=

Linux Extended Verification Module

- [Integrity Measurement Architecture (IMA)](https://sourceforge.net/p/linux-ima/wiki/Home/)

保护 [IMA](@linux-ima) 防止离线篡改（offline tampering）。

### Linux IMA

(linux-ima)=

Linux Integrity Measurement Architecture

[Linux IMA](@linux-ima) 子系统在内核中提供了一系列 hooks，可以用在在打开文件后（读取前）采集文件的哈希值。

- [How to use the Linux kernel's Integrity Measurement Architecture](https://www.redhat.com/en/blog/how-use-linux-kernels-integrity-measurement-architecture)
- [Integrity Measurement Architecture (IMA)](https://sourceforge.net/p/linux-ima/wiki/Home/)

### Linux Secure Memory

(linux-secure-memory)=

Linux Kernel Secure Memory

为 Linux 中的进程间内存共享提供一些安全选项，实现内存隔离保护。

- [Keeping secrets in memfd areas](https://lwn.net/Articles/812325/)
- [memfd_secret() in 5.14](https://lwn.net/Articles/865256/)

### Linux UGO

User, Group, Other

针对当前用户、所在组、其他组用户三种维度设置 RWX 三权限控制。
用户粒度较粗，如需更细致的粒度可用 Linux ACL。

### LPC

(lpc)=

Low Pin Count Bus

用于连接低速设备的总线。
这些低速设备有：BIOS，Super I/O，TPM。LPC 总线通常和主板上的南桥物理相连。

### LSM

(term_lsm)=

Linux Security Module

- [Linux Security Module Usage](https://www.kernel.org/doc/html/v4.16/admin-guide/LSM/index.html)
- [A BRIEF TOUR OF LINUX SECURITY MODULES](https://www.starlab.io/blog/a-brief-tour-of-linux-security-modules)

由 Linux 内核提供的一系列安全工具，包括：

- SELinux
- SMACK
- AppArmor
- TOMOYO
- Yama
- LoadPin
- SafeSetID
- Lockdown
- SARA
- KRSI

### LUKS

Linux 块存储加密标准，Linux Unified Key Setup

配合 cryptsetup 为块存储配置加密，提供 at-rest 的加密保护。

目前有两个版本：

- LUKS1:
- LUKS2: cryptsetup >= 2.1.0 时默认使用 LUKS2

### LXC

(lxc)=

LinuX Container

- [What's LXC?](https://linuxcontainers.org/lxc/introduction/)

指由 chroot、cgroup、apparmor 等 linux kernel 原生功能构建的容器。

### LXD

(lxd)=

- [What is LXD?](https://linuxcontainers.org/lxd/introduction/)
- <https://github.com/lxc/lxd>
- [LXD 2.0: Blog post series](https://stgraber.org/2016/03/11/lxd-2-0-blog-post-series-012/)

[LXC](@lxc) 的替代品，利用原生 linux kernel 的支持，既能提供 app container，
又能提供 system container。且 system container 的性能优于 hypervisor。

## M

(term_m)=

### MACI

(maci)=

Minimum Anti-Collusion Infrastructure

基于 [ZKP](@zkp) 实现的链上匿名投票方案。

### Memory Curtaining

(memory-curtaining)=

在[传统的内存保护技术](https://en.wikipedia.org/wiki/Memory_protection)以外，
为敏感数据提供完全隔离。

如：

- [Linux Kernel Secure Memory](@linux-secure-memory)

### Measurement

(measurement)=

度量

一般指通过哈希等方式度量程序的完整性，确保其内容没有被篡改。

### MAC

歧义：

- [Mandatory Access Control](@mac)
- [Memory Access Control](@mem_mac)
- [Message Authentication Codes](@msg_mac)

#### Mandatory Access Control

(mac)=

以 SELinux 为代表的强制访问控制

- [SELINUX AND MANDATORY ACCESS CONTROL (MAC)](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/virtualization_security_guide/sect-virtualization_security_guide-svirt-mac)

#### Memory Access Control

(mem_mac)=

64 位系统的使用 64 地址来寻址，但是因为[分级页表](@term_ptes)等技术，
实际上用来寻址的指令宽度是很少的（一般只有到 48 位），另外有很大一部分空间都是闲置的。

不仅如此，即使是 CPU 能用到的寻址空间里，实际真正会用到的位数也很少，在 RAM 寻址区内的指令也有相当长度是闲置的。
于是可以通过这些“闲置”的指令位，来防止一些 flags，用来对内存做安全加固或访问控制。
比如可以标记内存是属于 kernel/user，标记内存是否允许执行，等等。

![mem](https://s3.laisky.com/uploads/2022/09/mem-linear-addr.jpg)

不同 CPU 架构对内存标识位有不同的定义。

- ARM
  - UXN: Unprivileged Execute never
  - XN: Execute never
  - PXN: Privileged Execute never
  - PAC: Pointer Authentication
    - 通过增加发返回签名，来防御 [ROP](@rop)
  - BTI: Branch Target Instructions
    - 通过为代码打桩来防御 [JOP](@jop)
  - MTE: Memory Tagging
    - 通过为分配的内存打桩来提高安全性

#### Message Authentication Codes

(msg_mac)=

消息认证码，一般为消息体的哈希，用于计算消息完整性。

### MBR

(mbr)=

Master Boot Record

主引导记录，位于磁盘的第一个扇区，用于引导操作系统。被 [GPT](@gpt) 取代。

### MBZ

Must Be Zero

### MCU

(mcu)=

Micro Code Update

Intel 喜欢用 MCU 代表 Intel CPU 微码更新。

### MDS

(mds)=

微体系结构采样攻击, Microarchitectural Data Sampling

### MEE

(mee)=

内存加密引擎 Memory Encryption Engine

实现对数据 `in-use` 时的内存防护。

### MFA

(mfa)=

多因子认证 Multi-Factor Authentication

- [CISA: MFA](https://www.cisa.gov/sites/default/files/publications/MFA-Fact-Sheet-Jan22-508.pdf)

### MITM attack

(term_mitm_attack)=

中间人攻击，Man In The Middle

![mitm](https://s3.laisky.com/uploads/2022/08/MITM.png)

当双方进行握手和通信时，实际上并未建立点对点的连接，
而是有第三方插入其中，分别和双方建立通信。
所有的数据都流经第三方，第三方可以窃听甚至修改数据。

如 TLS 中，若服务端和客户端未校验对方的证书，那么就可能遭受 MITM 攻击。

### MLE

(mle)=

Measured Launch Environment

### MMIO

(mmio)=

Memory-Mapped I/O

将主存和外设的内存映射到同一个物理地址空间，所有的设备都监听总线，
当发现调用的地址属于自己时，就进行响应。

### MMU

(mmu)=

内存管理模块 Memory Management Unit

内存管理单元是介于处理器和片外存储器之间的中间层。提供对[虚拟地址（VA）](@term_va)向[物理地址（PA）](@term_pa)的转换。
一般封装于 CPU 芯片内部。

![mmu](https://s3.laisky.com/uploads/2022/08/mmu.png)

### Mode Setting

(mode_settings)=

显示模式设置

根据运行的位置，可以分为：

- 在用户空间运行的 [UMS](@ums)
- 在内核态运行的 [KMS](@kms)

KMS 的性能更好，且可以通过 KMS-API 和 libdrm 供用户态程序调用。

### MPA

(mpa)=

多方安全认证 Multi-Party Authorization

- <https://en.wikipedia.org/wiki/Multi-party_authorization>

对某个重要数据的解密，或某些重要功能的操作，需要不止一个人的授权。

### MPC

(mpc)=

多方安全计算，Secure Multi-party Computation

- [什么是多方安全计算 MPC？](https://zhuanlan.zhihu.com/p/315067912)

常见算法包括：

- [OT](@term_ot)
- [GC](@gc)
- [SS](@ss)

### MSRP

(msrp)=

Manufacturer's Suggested Retail Price

厂商建议零售价

### MSRs

(term_msrs)=

特殊模块寄存器 x86 Model Specific Registers

- [msr(4)](https://man7.org/linux/man-pages/man4/msr.4.html)

在 x86 架构处理器中，一系列用于控制 CPU 运行、功能开关、调试、跟踪程序执行、监测 CPU 性能等方面的寄存器。
通常应该由 kernel 来操作这些寄存器。

可以在 `/dev/cpu/CPUNUM/msr` 查看这些寄存器，使用前最好先用 `modprobe msr` 刷新。

### mTLS

(term_mtls)=

双向 TLS 认证，mutual TLS

客户端和服务端都准备好 TLS 证书，然后在握手阶段互相认证。

![mtls](https://s3.laisky.com/uploads/2022/08/illustration-tls-ssl-client-auth.png)

客户端证书可以让服务器确信客户端的身份，且可以防止 [MITM](@term_mitm_attack)。

服务端需要设置要求客户端提供证书并认证：

```go {hl_lines=["2-3"]}
tlsConfig := &tls.Config{
    ClientAuth: tls.RequireAndVerifyClientCert,
    ClientCAs: clientCAPool,
    Certificates: []tls.Certificate{
        {
            Certificate: [][]byte{cert},
            PrivateKey:  priv,
        },
    },
}
```

## N

(term_n)=

### NFV

(nfv)=

Network Function Virtualization

网络功能虚拟化（比如软路由？）

### NIST

(nist)=

美国国家标准与技术研究院 National Institute of Standards and Technology

负责制定各类美国联邦标准，在信息领域往往也是全球标准。

- <https://www.nist.gov/standards>

### Nitro

AWS 的硬件 TEE 解决方案

- [Confidential computing: an AWS perspective](https://aws.amazon.com/blogs/security/confidential-computing-an-aws-perspective/)

### NIZK

(nizk)=

Non-interactive zero-knowledge proofs

非交互式零知识证明。

### NNTP

Network News Transfer Protocol

### NSA

美国国家安全局, National Security Agency

### NTP

(ntp)=

Network Time Protocol

NTP 协议用来在不可靠的网络上同步时钟。

### NVIDIA APM

(nvidia_apm)=

Nvidia Ampere Protected Memory

微软为 Nvidia Ampere 架构（A100）推出的硬件内存加密功能，
支持将 GPU 纳入到 Azure TEE 环境内。

数据在 CPU TEE 中使用 GPU Driver 加密，
然后通过 PCIe 传输到 GPU 解密提供运算，
（说明 A100 上已经有 GPU AES 加密固件和内置硬件密钥）。
主要保护主存和 PCIe 传输安全。

![apm](https://s3.laisky.com/uploads/2022/09/nvidia-apm.png)

### NVIDIA CC

(nvidia_cc)=

Nvidia Confidential Computing

在 Hopper 架构的 NVIDIA H100 芯片中，引入了对机密计算的支持。

[Read More...](@page_nvidia_cc)

### NVIDIA MIG

(nvidia_mig)=

Nvidia Multi-Instance GPUs

- <https://blogs.nvidia.com/blog/2020/05/14/multi-instance-gpus/>
- [NVIDIA Multi-Instance GPU User Guide](https://docs.nvidia.com/datacenter/tesla/mig-user-guide/)
- [NVIDIA Multi-Instance GPU and NVIDIA Virtual Compute Server - Technical Brief.pdf](https://1drv.ms/b/s!Au45o0W1gVVLutZSUzlO7fmbgQerhg?e=pt6mvo)

英伟达在 Ampere 架构的 A100 芯片上推出的，可以让一个 GPU 最多创建 7 个并行计算的 GPU 实例，
实现多用户对一块 GPU 的共享。

MIG 能够为每一个租户实现完全独立的内存隔离。

> each instance’s processors have separate and isolated paths through the entire memory system - the on-chip crossbar ports, L2 cache banks, memory controllers, and DRAM address busses are all assigned uniquely to an individual instance.

![mig](https://s3.laisky.com/uploads/2022/09/gpu-mig-overview.jpg)

### NVIDIA Rot

Nvidia On-Die Root of Trust

感觉就是指 GPU driver 的 secure boot。
driver 会对 GPU 硬件进行度量。

### NVRAM

(nvram)=

非易失内存/持久化内存 Non-Volatile Memory

掉电也不会遗失数据，一般用于 HSM、TPM 等加密芯片的加密存储区。

## O

(term_o)=

### Occlum

(term_occlum)=

- <https://github.com/occlum/occlum>

蚂蚁金服开发的基于 [SGX](@intel_sgx) 的 [LibOS](@term_libos)。

[Read More...](@page_occlum)

### OC3

(oc3)=

Open Confidential Computing Conference

- <https://www.oc3.dev/>

### OCI

(term_oci)=

Open Container Initiative

- <https://opencontainers.org/>
- <https://github.com/opencontainers>

容器标准化组织，主要关注 container runtime 标准的组织

runtime 有时候会分为：

- 上层 runtime（[CRI](@term_cri)）：continerd + shim
- 底层 runtime（OCI）：OCI runtime

![cri](https://s3.laisky.com/uploads/2022/07/oci.jpeg)

分层设计，从下往上：

1. container：应用容器。
   一个抽象概念，只要具有 OCI SPEC 定义的标准属性和方法即可。
2. runtime：负责实际操作容器的一个可执行文件。
   该可执行文件的命令行参数必须符合 OCI Runtime 的标准。

   docker 默认的 runtime 是 runc，实现了 docker 容器。
   其他的还有 kata 实现了 vm 容器，
   gvisor 实现了 libos 容器。

3. shim：负责挂载 container stdin/stdout 的轻量级 daemon 进程。
   同时也是 runc 的封装，为更上次提供 ttrpc 调用接口。
4. containerd：这一层也被称为 CRI。
   负责管理 sandbox。（docker 领域的 sanbox 可以认为是容器 + 网络 + 镜像）。

   虽然会常驻后台负责响应更上层的操作，但是其进程和 container 进程没有依赖关系。

5. dockerd/kubelet：面向用户或 PaaS 平台的 agent。
   接收上层调度或用户指令，然后传输给 containerd。

### OCI Runtime

(term_oci_runtime)=

- [OCI runtime specification](https://github.com/opencontainers/runtime-spec)

![oci](https://s3.laisky.com/uploads/2022/07/runc.drawio.png)

1. 上游（kubelet/dockerd）调用 containerd 启动/操作容器
2. containerd 通过 exec 启动 shim 可执行文件。
   传递参数 `--address, --namespace, --id`
3. shim fork 出 shim-daemon。
   shim 退出，shim-daemon 常驻后台，生命周期捆绑 container。
4. shim-daemon 调用 runc 可执行文件。
   用 `--detach` 模式调用 runc，runc 启动容器后退出，
   将容器的 stdin/stdout 挂载到 shim-daemon，然后 runc 退出。
5. runc 负责实现 container 的标准 OCI 接口。
   runc 以外的组件并不需要关心 container 的具体实现方式，可能是 docker/vm/libos。
6. 因为 runc 退出，container 被挂载到 shim-daemon。
7. shim-daemon 创建 socket 文件，监听来自 containerd 的操作。
   socket 文件的位置在 `/var/run/containerd/s/<hash>`。

   `hash = sha256(address, ns, id)`

### OEM

Original Equipment Manufacturer

### OID

(oid)=

Object Identifier

- [search OID assignments from the top node](https://www.alvestrand.no/objectid/top.html)
- [What is an object identifier?](https://www.alvestrand.no/objectid/)
- [How To Get Your Own OID](https://ldapwiki.com/wiki/How%20To%20Get%20Your%20Own%20OID)
- [Reserved for OID 1.3.9900](https://oidref.com/1.3.9900)

### OpenEnclave

(term_openenclave)=

微软主导的 SGX Enclave Runtime。

[Read More...](@page_sgx_openenclave)

### ORAM

(oram)=

不经意内存存取，Oblivious RAM

- [AN INTRODUCTION TO OBLIVIOUS RAM (ORAM)](https://research.kudelskisecurity.com/2020/04/22/an-introduction-to-oblivious-ram-oram/)

### OT

(term_ot)=

不经意传输, Oblivious Transfer

### OTA

在线升级，Over The Air

## P

(term_p)=

### PA

(term_pa)=

物理内存地址，Physical memory Address

也称为：

- [HPA](@term_host_phy_addr)

### Package

(term_package)=

指 CPU 芯片。

- Single-Package Platform：单 CPU 机器
- Multi-Package Platform：多 CPU 机器

### Passwordless

[Read More...](@page_passwordless)

### PCI

(pci)=

支付卡行业, Payment Card Industry

几大信用卡支付机构（VISA、MasterCard、AE、Discover、JCB）的联盟。

下辖机构：

- [SSC](@pci_ssc)

### PCI DSS

(pci_dss)=

支付卡数据安全标准, PCI Data Security Standard

由 [PCI SSC](@pci_ssc) 制定。

### PCI SSC

(pci_ssc)=

支付卡产业安全标准委员会, PCI Security Standards Council

制定了一系列安全标准，包括：

- [PCI DSS](@pci_dss)

### PCT

(pct)=

隐私计算技术 Privacy Computing Technology

### PFS

(pfs)=

前向保密 Perfect Forward Secrecy

当攻击者取得了私钥，是否可以解开历史上所有的通讯密文？

RSA 不具有 PFS，[ECC](@ecc) 则有。

### PGD

(term_pgd)=

页全局目录, Page Global Directory

Linux 四级分页结构的第一层，[详见 PTEs](@term_ptes)

### PHE

(phe)=

半同态加密，Partial Homomorphic Encryption

### PHI

(phi)=

受保护健康信息, Protected Health Information

能够与特定个人关联，由受保护实体（或受保护实体的业务关联企业）创建或收集的有关健康状况、医疗保健提供或医疗保健支付的任何信息。PHI 涵盖的内容极为广泛，包括病人的医疗记录或支付历史的任何部分。

### PII

(pii)=

个人可识别信息，Personally Identifiable Information

### PIR

(term_pir)=

Private Information Retrieval

- [Wiki: Private information retrieval](https://en.wikipedia.org/wiki/Private_information_retrieval)
- [隐私信息检索方案汇总分析](https://www.freebuf.com/articles/323426.html)

检索方希望向数据拥有方查询数据，但是不希望拥有方知道是什么数据被查询了。

实现方式有：

- [不经意传输](@term_ot)
- 基于[同态加密](@he)
- keyword：模糊检索的实现

### PIV

(piv)=

个人识别信息 Personal Identity Verification

在信息安全领域一般指 PGP 等标记个人身份的公钥等。

- [NIST_SP-800-73-4_Interfaces for Personal Identity Verification.pdf](https://1drv.ms/b/s!Au45o0W1gVVLva17LAeKMstVZTGboA?e=K17joK)
- [PIV 的 NIST 标准汇总](https://csrc.nist.gov/projects/piv/piv-standards-and-supporting-documentation)

### PKC

Public Key Cryptography

### PKI

(term_pki)=

Public Key Infrastructure

用于管理密钥签发和公钥认证、吊销的基础设施。

### PKIX

(term_pkix)=

Public-Key Infrastructure using X.509

- [RFC-5280](https://www.rfc-editor.org/rfc/rfc5280.html)

由 IETF PKIX 工作组提出了融合 X.509 v3 证书和 X.509 v2 [CRL](@term_crl) 的标准。

### PMH

(term_pmh)=

Page Missing Handler

发生 `#PF` 时负责加载页的程序，属于 [MMU](@mmu) 的一部分

### PMP

Physical Memory Protection

### PPID

(ppid)=

Platform Provisioning ID

> Unique Provisioning ID of the processor package or platform instance.

PPID 不属于 [TCB](@tcb)。

### PPM

(ppm)=

Parallel Programming Model

- <https://en.wikipedia.org/wiki/Parallel_programming_model>

并行计算模型，包括：

- [SIMD](@simd)
- [SIMT](@simt)
- [SMT](@smt)

### Process Image

- <https://tldp.org/LDP/LG/issue23/flower/psimage.html>

可执行文件（如 ELF）被分配了地址空间后的状态，称为 Procss Image。
当进程被切换时用于保存上下文，期间只读不可变更，待进程重入（re-entrant）时用于恢复进程执行。

### Protect Rings

(term_protect_rings)=

保护环，是 [HPD](@term_hpd) 的同义词。

### PSD

Payment Services Directive

### PSI

(psi)=

隐私保护集合交集 Private Set Intersection

- [多方安全计算：隐私保护集合求交技术](https://blog.csdn.net/devcloud/article/details/117113696)

### PTEs

(term_ptes)=

页表项，Page Table Entries

每一项代表物理内存的每一帧，通过 `Frame Number` 来索引。

![ptes](https://s3.laisky.com/uploads/2022/08/ptes.png)

Linux 采用四级页表来节省指令空间，每级页表占 9 bit，一共 36 bit 实现了 `(2^9)^4` 的空间，
每一页按 4KB 计算，即实现了对 `281,474,976,710,656 bit` 的寻址（256 TB）。
所以一个 64 bit 的指令宽度里，实际上只有 36 bit 用于寻址，这一宽度也被称为 `MAXPHYADDR`

{{< katex >}}
{2^9}^4 _4_ 1024 = 281,474,976,710,656
{{< /katex >}}

内存页表存在于内核中，创建进程的时候，内核会将页表拷贝至进程地址空间内的随机位置，
`CR3` 指向第一级页表 `PGD` 的位置。

所以每次寻址的路径是：

1. CR3
2. PGD: Page Global Directory
3. PUD: Page Upper Directory
4. PMD: Page Middle Directory
5. PTE: Page Table Entries
6. [PA](@term_pa)

![pte](https://s3.laisky.com/uploads/2022/08/linux_four_level.jpg)

## Q

(term_q)=

### QMP

QEMU Machine Protocol

- <https://wiki.qemu.org/Documentation/QMP>

## R

(term_r)=

### RADIUS

(radius)=

Remote Authentication Dial-In User Service, 远程用户认证服务

也被称为 [AAA](@aaa)。

### RA

歧义：

- [Registration Authority](@x509_ra)
- [Remote Attestation](@remote-attestation)

#### Registration Authority

(x509_ra)=

#### Remote Attestation

(remote-attestation)=

- <https://en.wikipedia.org/wiki/Trusted_Computing#Remote_attestation>
- [Secure Remote Attestation.pdf](https://1drv.ms/b/s!Au45o0W1gVVLuokCRkfAmodZMAqQZA?e=87GloV)

计算机硬件验证软件完整性的一种方式。硬件利用内置私钥对执行中的软件计算签名，
发送给远程服务提供商进行验签。

可能遭受 [ASA 攻击](@asa)

- [TPM](@tpm) [Remote Attestation](@remote-attestation) 的 Golang 实现：
  - [TPM REMOTE ATTESTATION PROTOCOL USING GO-TPM AND GRPC](https://blog.salrashid.dev/articles/2021/tpm_grpc/)
  - <https://github.com/google/go-attestation>
- [SGX Remote Attestation](@intel_sgx_remote_attestation)

### RAG

(rag)=

Retrieval-Augmented Generation

在 LLM 中，RAG 指借助 embeddings 向量数据库（vector db）等方式实现的，依赖外部知识库的文本生成。

### RATLS

(ratls)=

Remote Attestion based TLS

对 [TEE](@tee) 应用建立基于远程认证的 TLS 连接

### Register

(term_register)=

常用寄存器([GPR](@gpr))：

- `%rax`: 临时变量，如保存 syscall 值和返回值
- `%rbx`:
- `%rcx`: 曾用于保存第四个参数，后被用来保存返回地址，被 %r10 取代
- `%rdx`: 第三个参数
- `%rsp`: stack pointer
- `%rbp`:
- `%rsi`: 第二个参数
- `%rdi`: 第一个参数
- `%rip`: instruction pointer
- `%eip`: extended instruction pointer，一般用于存储函数返回地址
- `%r8`: 第五个参数
- `%r9`: 第六个参数
- `%r10`: 第四个参数

![register](https://s3.laisky.com/uploads/twitter/14/eb/FZ14-sWVsAALuws.png)

[MSR](@term_msrs):

- 段寄存器:
  - CS: Code Segment (used for IP)
  - DS: Data Segment (used for MOV)
  - ES: Destination Segment (used for MOVS, etc.)
  - SS: Stack Segment (used for SP)
  - FS: TLS 地址
  - GS: GDT 地址
- CR3: 指向 [PGD](@term_pgd)

扩展阅读：

- [assembly - What is the "FS"/"GS" register intended for? - Stack Overflow](https://www.notion.so/laisky/assembly-What-is-the-FS-GS-register-intended-for-Stack-Overflow-6506a543650b4252a859fffad21434c0)

### RNG

随机数生成 Random Number Generation

### RoHS

Restriction of Hazardous Substances

RoHS 是由欧盟立法制定的一项强制性标准，它的全称是《关于限制在电子电气设备中使用某些有害成分的指令》(Restriction of Hazardous Substances)。 该标准已于 2006 年 7 月 1 日开始正式实施，主要用于规范电子电气产品的材料及工艺标准，使之更加有利于人体健康及环境保护。

### ROP

(rop)=

返回导向编程，Return-Oriented Programming

[CRA](@cra) 的一种，恶意攻击者在函数中篡改 [`%eip`](@term_register) 的值，来让函数结束后跳转执行代码。

### RoT

(rot)=

Root of Trust

一般被用来描述硬件信任根，是硬件 [TEE](@tee) 的基石。有两大职责：

1. 可信度量（trusted measurement）
2. 可信评估（trust score）

可信度量记录下不可篡改的度量值，而可信评估作为一个接口，可以给 verifier 调用以查看可信度量的结果。

### RTC

实时时钟，Real-Time Clock

### RTM

[RoT](@rot) for Measurement

## S

(term_s)=

### SA

(sa)=

Subversion Attack

是 [ASA](@asa) 的同义词。

### SC

(sc)=

Sub Committee

### Secure Boot

(secure-boot)=

由 BIOS 硬件在启动时检查 UEFI 驱动、操作系统、EFI 应用等软件的签名。
确保所启动的系统是受信任的。

```plaintext
secure boot
├── firmware
└── kernel
    ├── sanbox
    ├── IMA
    └── TEE
```

### SEE

Secure Execution Environment

### Segement

(term_mem_segment)=

1966 年古老的 Multics 系统的历史遗留，在分页（paging）出现以前的内存隔离方法。
将不同程序的内存映射到物理内存不同的段（segment）上以实现隔离。

过去指令宽度过窄，导致寻址空间有限，也需要靠分段来扩大寻址空间。
高位地址定位段基址，低位定位段内偏移。

寻址时通过 `Segment Base + offset` 来实现。
这种地址也被称为 `logical address`。

缺点是粒度过粗，已经被分页或段页制等技术替换。

因为现代芯片支持的指令已经够宽，换言之，能支撑的寻址空间大到不需要再分段。
现代 Linux 等多使用平坦（flat）模式，即将所有的段基址都设置为 0。
实际上就是所有的段都互相重叠，覆盖所有内存空间，寻址完全依赖偏移量来实现。

### SELinux MCS

SELinux Multi-Category Security

- [Why you should be using Multi-Category Security for your Linux containers](https://www.redhat.com/en/blog/why-you-should-be-using-multi-category-security-your-linux-containers)

### SCI

(sys_sci)=

System Call Interface

见 [syscall](@term_syscall)

### SDL

(sdl)=

Secure Development Lifecycle, 安全开发生命周期

（有时候也称为 SDLC，LifeCycle）

- [Secure Development Lifecycle: The essential guide to safe software pipelines](https://techbeacon.com/security/secure-development-lifecycle-essential-guide-safe-software-pipelines)

> the SDL is a process that standardizes security best practices across a range of products and/or applications.

2002 年由微软发布的概念，可以简单理解为开箱即用的安全最佳实践。

### SFI

(term_sfi)=

Software-based Fault Isolation

- [SFI - Principles and Implementation Techniques of Software-Based Fault Isolation.pdf](https://1drv.ms/b/s!Au45o0W1gVVLurh1YmaybF9eG5F-pQ?e=jcQwHF)

由用户态软件实现的 Sandbox 技术，统称为 SFI。

标志性实现：

- [NaCl: Google Native Client](https://zh.m.wikipedia.org/zh/Native_Client#:~:text=Google%20Native%20Client%EF%BC%88%E7%B8%AE%E5%AF%AB%E7%82%BA,%E5%9C%A8%E6%B2%99%E7%9B%92%E4%B8%8A%E9%81%8B%E8%A1%8C%E3%80%82)

### SGX

见 [Intel SGX](@intel_sgx)。

### Side Channel Attack

(term_side_channel_attack)=

侧信道攻击

- [Wiki: Side-channel attack](https://en.wikipedia.org/wiki/Side-channel_attack)

包括：

- [Cold boot attack](https://en.wikipedia.org/wiki/Cold_boot_attack): 从断电的内存条中恢复数据
- timing attack: 计时攻击，通过计算耗时不同来探测敏感信息
- power-monitoring attack: 通过耗电量不同来嗅探

### SIMD

(simd)=

Single Instruction Multiple Data

属于 [PPM](@ppm) 范畴。

### SIMT

(simt)=

Single Instruction Multiple Threads

属于 [PPM](@ppm) 范畴，单指令多线程并行计算，如 CUDA 中的 Block、Thread 计算。

### SINH

(sinh)=

中国科学院上海营养与健康研究所

![sinh](https://s3.laisky.com/uploads/2022/05/sinh.png)

- <http://www.sinh.cas.cn/>

### SKPP

Separation Kernel Protection Profile

一种基于 kernel 隔离的 [TEE](@tee) 构建思想，主要功能有：

1. Data Separation：数据隔离
2. Sanitization：共享资源不能被用于泄漏信息
3. Control of Information Flow：隔离区互相不能随意通信
4. Fault Isolation：某个隔离区被攻破，不会影响其他隔离区

### SLAT

(term_slat)=

二级地址转换, Second Level Address Translation

- [Wiki: Second Level Address Translation](https://en.wikipedia.org/wiki/Second_Level_Address_Translation)

实现：

- [Intel EPT](@term_intel_ept)
- [AMD RVI](@term_amd_rvi)

### SMC

- [Secure Multiparty Computing](@secure_mc)
- [System Management Controller](@smc)

#### Secure Multiparty Computing

(secure_mc)=

安全多方计算

#### System Management Controller

(smc)=

系统管理控制器

### SMM

(smm)=

System Management Mode

### SMT

(smt)=

Simultaneous Multi-Threading

属于 [PPM](@ppm) 范畴。

### SoC

歧义：

- [Security Operations Center](@soc_team)
- [System On Chip](@soc)

#### Security Operations Center

(soc_team)=

- [What is a Security Operations Center (SOC)](https://www.ibm.com/topics/security-operations-center)

24 小时安全响应团队，也称为 [ISOC](@isoc)

#### System On Chip

(soc)=

系统级芯片 System On Chip

在一块芯片上集成一整个信息处理系统，称为片上系统或系统级芯片。这个定义现在也不尽明确，因为不同用途的 SoC 上集成的部件是不一样的，一般说来，SoC 是一个完整的整体，已经拥有了整个数字系统的完整功能它也是一种 ASIC，其中包含完整的控制系统并有嵌入式的软件。

### Socket

CPU 插槽。

假设一个平台（Platform）上有多个 CPU（[Package](@term_package)），
这些 CPU 在不同的插槽（Socket）上有多种不同的安装方法。

### SoK

(sok)=

Systematization of Knowledge Papers

如果论文标题以 `SoK:` 开头，代表这是一篇综述性论文

### SPA

(spa)=

System Physical Address

见 [hpa](@term_host_phy_addr)

### SPI

(spi)=

Serial Peripheral Interface

串行外围设备接口。是 Motorola 首先在其 MC68HCXX 系列处理器上定义的。SPI 接口主要应用在 EEPROM，FLASH，实时时钟，AD 转换器，还有数字信号处理器和数字信号解码器之间。SPI，是一种高速的，全双工，同步的通信总线，并且在芯片的管脚上只占用四根线，节约了芯片的管脚，同时为 PCB 的布局上节省空间。

### SS

(ss)=

秘密共享，Secret Sharing

### SSC

(ssc)=

上海计算机软件技术开发中心

![ssc](https://s3.laisky.com/uploads/2022/05/ssc.jpg)

### SSE

对称可搜索加密, Searchable Symmetric Encryption

- [对称可搜索加密技术研究进展.pdf](https://1drv.ms/b/s!Au45o0W1gVVLutwxKAu9O7Ve5zA1UQ?e=vG0ZD7)

### SSN

(ssn)=

Social Security Number

相当于美国的身份卡号

> a nine-digit number that the United States government issues to U.S. citizens and eligible residents.

### SSS

(sss)=

Shamir's Secret Sharing

一种密钥分享算法，假设有 L 个参与者，可以设定当人数大于等于 K（K 小于 L）时，即可还原出密钥。

属于 [Threshold Cryptosystem](@tc2) 的一种具体实现。

### STM

(stm)=

Software Transactional Memory

- [Wiki: Software transactional memory](https://en.wikipedia.org/wiki/Software_transactional_memory)

软件事务内存（STM）是一种类似于数据库事务的并发控制机制，用于控制并发计算中对共享内存的访问。它是锁定同步的替代方案。STM 是一种在软件中实现的策略，而不是作为硬件组件存在。

### STRIDE

(term_stride)=

威胁模型分析模型，指:

- Spoofing identity
- Tampering with data
- Repudiation
- Information disclosure
- Denial of service
- Elevation of privilege

### SV

(sv)=

Starting Variable

是 [IV](@iv) 的同义词。

### SVSM

(svsm)=

Secure VM Service Module

利用 [AMD SEV-SNP](@amd_sev_snp) 的 [VMPL](@amd_sev_vmpls) 技术，
可以在 CVM 内以 VMPL0 权限运行一个特权管理器，拦截监听 VM 的一切 syscall 和内存操作。

### Syscall

(term_syscall)=

系统调用，System Call

同义词：[SCI](@sys_sci)。

- [Sysenter Based System Call Mechanism in Linux 2.6](http://articles.manugarg.com/systemcallinlinux2_6.html)

用户程序和 kernel 运行于不同的 [HPD](@term_hpd)，
kernel 运行于 `Ring-0` 拥有对硬件的管理权限，
用户程序运行于 `Ring-3` 只有执行计算任务的权限，
若用户程序需要操作硬件等特权操作，就只能通过 kernel 像用户态暴露的一组 system call 来完成。

Kernel 暴露给用户态的 ABI 接口。通过 [ECF](@term_ecf) 流程中的 `trap` 来实现。

流程：

1. 将相关 syscall 号分别存入 `%rax` 和 `%orig_rax`。

   存两次因为启动 syscall 时，`%rax` 会保存 syscall 号，
   在 syscall 结束后，`%rax` 会保存执行结果。
   为了保留 syscall 号不被覆盖，会在 `%orig_rax` 额外存一份 syscall 号。

2. 把最多六个参数存入 `%rdi`, `%rsi`, `%rdx`, `%r10`, `%r8`, `%r9`
3. 通过 `sysenter` 切换到内核态，kernel 查找并执行相应的 syscall 函数
4. 执行结果存入 `%rax`，`sysexit` 回到用户态

- [syscall 速查表](https://filippo.io/linux-syscall-table/)

linux 2.6 以前用 `0x80` 来启动 syscall，后来因为性能太差，以及会干扰其他中断，
换用 `sysenter` 指令。

- x86-32:

  - Intel: `0x80`、`sysenter/sysexit`
  - AMD: `0x80`、`syscall/sysret`

- x86-64: `syscall`

## T

(term_t)=

### TA

时间自动机，Timed Automata

### TC

歧义：

- [Threshold Cryptography](@tc2)
- [Trusted Computing](@tc)

### Threshold Cryptography

(tc2)=

门限密码学

假设有 L 个参与方进行加密，只需要 K（K < L）个参与方即可实现解密。

#### Trusted Computing

(tc)=

可信计算

- [What is Trusted Computing?](https://cs.stanford.edu/people/eroberts/cs201/projects/trusted-computing/what.html)
- [Wiki: Trusted_Computing](https://en.wikipedia.org/wiki/Trusted_Computing)
- [看见“信任”，可信计算平台的由来解读（TPM、TCM、TPCM、等保 2.0 解读）](https://icode.best/i/18519245017325)

主要内容包含：

- [Endorsement Key](@tpm-ek)
- Secure Input/Output
- [Memory Curtaining](@memory-curtaining)
- [Sealed Storage](@intel_sgx_sealing)
- [Remote Attestation](@remote-attestation)

主要领域包括：

- [TPM](@tpm)/[TCM](@tpm)/TPCM
- [TCG Software Stack](@term_tcg_software_stack)
- [TNC](@tnc)

> Trusted Computing allows a piece of data to dictate what Operating System and Application must be used to open it.
>
> 可信计算让数据可以决定由什么操作系统和程序来使用它。

通俗来讲，可信就是在每台 PC 机启动时检测 BIOS 和操作系统的完整性和正确性，保障你在使用 PC 时硬件配置和操作系统没有被篡改过，所有系统的安全措施和设置都不会被绕过。
可信主要通过度量和验证的技术手段实现。 度量（Measurement）就是采集所检测的软件或系统的状态，验证是将度量结果和参考值比对看是否一致。

度量分为[动态度量](@tpm-drtm)和[静态度量](@tpm-srtm)。

- [How does the TPM perform integrity measurements on a system?](https://security.stackexchange.com/a/44350/200559)

可信链（chian of measurements）:

![chians](https://s3.laisky.com/uploads/2022/05/tc.png)

### TCB

(tcb)=

可信计算基 Trusted Computing Base

指达成可信所需要保护的内容有哪些。
一般来说 TCB 越小，安全性越高。

如 hypervisor 的 TCB 就是整个虚拟化系统。SGX 的 TCB 就是 enclave。

### TCG

(tcg)=

Trusted Computing Group

- <https://trustedcomputinggroup.org/>

国际可信计算组织，提出了 [TCM](@tpm) 等标准。

### TCM

Trusted Cryptography Module

对标 [TPM](@tpm)，属于中国自主可信计算系列产品。

### TDISP

(tdisp)=

TEE Device Interface Security Protocol

为了解决传统 [CVM](@cvm) 加密内存和外设间通过 shared memory（bounce buffer）共享的低效问题，
同时也是为了解决 CVM 和 PCIe 外设间的加密通讯问题。AMD 和 PCI SIG 共同协作推出了 TDISP。

TDISP 使得受信任的外设可以直接操作 CVM 内的 private memory，从而提高了 I/O 性能。

![](https://s3.laisky.com/uploads/2023/07/trust-device-access.png)

设备（DSM）可以被定义为多个 TDIs，然后这些 TDIs 可以被分配给 CVM，
被 CVM 视为可信设备，直接操作 CVM 的 private memory。

![](https://s3.laisky.com/uploads/2023/07/tdisp.png)

### TDISP DSM

(dsm)=

Device Security Module

[TDISP](@tdisp) 中，受信任的外部设备称为 DSM。
每一个 DSM 可以创建一个或多个 [TDI](@tdi)。

### TDISP SPDM

(spdm)=

Secure Protocol and Data Model

TDISP 中，TSM 和 DSM 间的可信通讯协议。

### TDISP TDI

(tdi)=

TEE Device Interfaces

[TDISP](@tdisp) 中，[DSM](@dsm) 可以创建多个 TDI，
TDI 可以绑定到 CVM 中。

### TDISP TSM

(tsm)=

TEE Security Module

> which is responsible for configuration of the host isolation controls
> protecting guests from the Virtual Machine Monitor (VMM) and other host software.
> The TSM also drives the lifecycle of a TDISP enabled device through the configuration,
> binding, and unbinding of TDIs to guests.

### TECC

可信密态计算，Trusted-Environment-based Cryptographic Computing

- [可信密态计算白皮书-2022.pdf](https://1drv.ms/b/s!Au45o0W1gVVLutwO1RT6eLUTOxwHCw?e=G6kuW1)

蚂蚁提出的 TEE 方案

### TEE

(tee)=

可信执行环境, Trusted Execution Environment

通过隔离或加密，实现 in-use 的数据安全防护。
一般采用以硬件为基础的防护方案。

[More...](@xss_tee)

### TLB

(term_tlb)=

Translation Lookaside Buffer

虚拟内存地址和物理内存地址对应关系的缓存

![tlb](https://s3.laisky.com/uploads/2022/08/tlb.png)

![tlb](https://s3.laisky.com/uploads/2022/08/tlb-2.png)

### TLS

歧义:

- [Thread Local Storage](@term_thread_local_storage)
- [Transport Layer Security](@term_tls)

#### Thread Local Storage

(term_thread_local_storage)=

线程除了堆栈外的一些上下文信息，kernel 中为每一个线程都维护了一个 TLS。

- [[announce, patch] Thread-Local Storage (TLS) support for Linux, 2.5.28](https://lwn.net/Articles/5851/)

  2.5 时代的 kernel 用 [LDT](@term_ldt) 来保存线程上下文，但是 [GDT](@term_gdt) 中只有 8192 个 [LDT](@term_ldt)，
  导致进程最多只能有 8192 个线程。

#### Transport Layer Security

(term_tls)=

Transport Layer Security

- [RFC 8446: The Transport Layer Security (TLS) Protocol Version 1.3](https://www.rfc-editor.org/rfc/rfc8446)

基于非对称密钥进行密钥协商的安全传输协议，用于代替 SSL。现行标准为 v1.3。

TLS 无法防止 [MITM 攻击](@term_mitm_attack)，需要依靠 [PKI](@term_pki)。

### TLS CCA

(term_tls_cca)=

TLS 客户端证书认证，TLS Client Certificate Authentication

见 [mTLS](@term_mtls)。

### TNC

(tnc)=

可信网络连接 Trusted Network Connect

用来实现平台到网络的可信扩展，以确保网络的可信。

### TOS

Trusted Operating System

### TOTP

Time-based One-Time Password

### TPM

(tpm)=

Trusted Platform Module(TPM, also known as ISO/IEC 11889)，由 [TCG](@tcg) 制定

- [TPM 2.0 Library](https://trustedcomputinggroup.org/resource/tpm-library-specification/)

是一项[安全密码处理器](https://zh.wikipedia.org/w/index.php?title=%E5%AE%89%E5%85%A8%E5%AF%86%E7%A0%81%E5%A4%84%E7%90%86%E5%99%A8&action=edit&redlink=1)的[国际标准](https://zh.wikipedia.org/wiki/%E5%9B%BD%E9%99%85%E6%A0%87%E5%87%86)，核心功能在于记录基于 PCR 信任链的[静态度量](@tpm-srtm)和[动态度量](@tpm-drtm)。

TPM 通过 [LPC](@lpc) 或 [SPI](@spi) 总线连接到 CPU，只允许 CPU 访问，不允许外部访问。

除了度量外，TPM 还需要通过 [RA](@remote-attestation) 来证明自己的可信，这通过其内部存储的一系列密钥来实现：

{{< hint info >}}
TPM 1.2 及以前采用 `EK -- PCA --> AIK` 的方式进行 RA。
TPM 2.0 改用 `EK --> SRK --> AK` 的方式。
{{</ hint >}}

- [Endorsement Key](@tpm-ek)
- [Storage Root Key](@term_tpm_srk)
- [Attestation Keys](@term_tpm_ak)

为了和 [vTPM](@vtpm) 区分，有时候被称为 pTPM（physical TPM）。

### TPM AIK

(tpm_aik)=

TPM Attestation Identity Keys

TPM 1.2 及之前版本的 RA 密钥，在 2.0 中已经被 [AK](@term_tpm_ak) 取代。

- <https://security.stackexchange.com/a/204271/200559>
- [What's the difference between the endorsement key and the attestation identity key within the TPM?](https://security.stackexchange.com/a/235391/200559)

### TPM AK

(term_tpm_ak)=

TPM Attestation Keys

[AK](@intel_sgx_ak) 可供用户使用，用来证明数据是由一个可信 TPM 签发的。

存在第三方的 Attestation CA，提供信任链校验 [AK](@intel_sgx_ak) Certificates。

### TPM CRTM

(tpm-crtm)=

核心信任根 Core Root of Trust for Measurements

TPM 启动时度量的第一个东西被称为 CRTM。

BIOS 启动时将会度量 BIOS，并将哈希值存入 [PCR](@tpm-pcr) 0 的位置，
作为可信链的第一环。

### TPM DRTM

(tpm-drtm)=

动态度量, Dynamic Root of Trust for Measurements

动态度量和验证指在系统运行时动态获取其运行特征，根据规则或模型分析判断系统是否运行正常。

动态度量和静态度量最大的区别就是，它可以在一个不安全的环境中，动态的创建出一个可信的执行环境来。
Intel 的实现称为 [Intel TXT](@intel-txt)、AMD 的实现称为 [SVM](@amd-svm)

### TPM EA

TPM Extended Authorization

### TPM EK

(tpm-ek)=

TPM Endorsement Key

内置于 TPM 硬件中，不可变更的一组非对称密钥和证书。
可用来作为当前 TPM 的身份标识。

因为其不可变更，所以不允许用户将其用来签名。
（机器的用户可能会变，而 EK 永远不变，所以不会用来加密用户数据）。

用户数据采用 [AK](@intel_sgx_ak) 加密

### TPM Fragility

(tpm_fragility)=

TPM Sealing 绑定到特定 PCR 时，会导致 BIOS、OS 等被锁死，
任何变动都会导致 TPM 无法 UnSealing。

这一情况也称为 TPM Brittle/Brittleness。

TPM2.0 的 `TPM2_PolicyAuthorize` 命令（也称为 `wild card policy`）允许通过非对称签名绑定 BIOS、Kernel，
而不仅仅是静态的 SHA。

### TPM PCA

TPM Privacy CA

签发 [AIK](@tpm_aik) 的重要参与角色，负责校验 EK，并签发 AIK 的 CSR 生成证书。

### TPM PCR

(tpm-pcr)=

TPM Platform Configuration Registers

- [A Practical Guide to TPM 2.0: Platform Configuration Registers](https://link.springer.com/chapter/10.1007/978-1-4302-6584-9_12)

一组 TPM 的寄存器，用来存放系统从启动开始的一系列采样哈希值，
可以用来表征系统运行至今的状态历史（启动链），用作完整性证明。

每一个 PCR 在系统启动时创建，append-only，只允许清空或扩展，不允许修改。

TPM 2.0 规范要求 TPM 硬件应该至少有 24 个 PCRs，且支持 SHA-256 和 SHA-384。

![tpm-pcr-number](https://s3.laisky.com/uploads/2023/04/tpm-pcr-number.png)

[SRTM](@tpm-srtm)/[LCP](@lcp):

- PCR0 – CRTM, BIOS code, and Host Platform Extensions[a]
- PCR1 – Host Platform Configuration
- PCR2 – Option ROM Code
- PCR3 – Option ROM Configuration and Data
- PCR4 – IPL (Initial Program Loader) Code (usually the Master Boot Record – MBR)
- PCR5 – IPL Code Configuration and Data (for use by the IPL Code)
- PCR6 – State Transition and Wake Events
- PCR7 – Host Platform Manufacturer Control

[DRTM](@tpm-drtm)/[MLE](@mle):

- PCR17 – DRTM and launch control policy
- PCR18 – Trusted OS start-up code (MLE)
- PCR19 – Trusted OS (for example OS configuration)
- PCR20 – Trusted OS (for example OS Kernel and other code)
- PCR21 – as defined by the Trusted OS
- PCR22 – as defined by the Trusted OS

### TPM PCR Bank

假如一个 TPM 芯片支持 24 的 PCRs，它在逻辑上会显示为 SHA-256、SHA-384 两个 banks，
且每一个 bank 都有 24 个 PCRs。
但实际上你只能选用一个 bank，修改任何 bank 内的 PCR，都会影响到所有 banks 中具有相同索引值的 PCR。

### TPM Seeds

TPM 2.0 不再直接保存 SRK 等密钥，而是存储三个 seeds：storage seed、endorsement seed、platform seed。
这三个 seed 作为烧录进硬件的私钥，根据用户传入的 template 可以派生出无数个 primary key。
用户派生的 primary key 默认存储于易失介质中，掉电就会丢失，用户也可以通过 FLUSH 手动清除。
用户可以将数量有限的 primary key 保存在持久化介质中。

这些 primary key 可以视为 TPM 1.2 中的 EK 和 SRK。
可以认为，TPM 2.0 是 TPM 1.2 的超集，等效于 N 个 TPM 1.2。

### TPM SRK

(term_tpm_srk)=

TPM Storage Root Key

TPM 为每个用户生成一个 SRK，用来加密存储持久化数据。

### TPM SRTM

(tpm-srtm)=

静态度量, TPM Static Root of Trust for Measurements

静态度量指的是从机器启动之初到 OS 启动的这个过程中，对各个阶段的系统状态进行度量，并将度量值存储在 TPM 的 [PCR](@tpm-pcr) 中。
每一个 PCR 都对应一个 SHA-256/384 的哈希值，
这个哈希值由从启动之初至今的全部度量数据计算得出（即后一个 PCR 会包含前面所有 PCR 的度量数据）。
所有的 PCR 组成了一个信任链，用来证明系统启动过程中的完整性。

### TPM TS

TPM Software Stack Specifications

### TPN

时间 Petri 网，Timed Petri Net

### TPU

Tensor Processing Unit

张量处理器，Google 为机器学习定制的专用芯片。

### TRNG

(trng)=

真随机数发生器，True Random Number Generator

### TSP

汽车远程服务提供商，Telematics Service Provider

汽车车机、车联网系统的服务提供商，提供远程服务。

### TSS

歧义:

- [Task State Segment](@term_task_state_segment)
- [TCG Software Stack](@term_tcg_software_stack)
- [Threshold Signature Scheme](@term_threshold_signature_scheme)

#### Task State Segment

(term_task_state_segment)=

用来保存一些 CPU 执行 task 的状态信息，保存在 [GDT](@term_gdt) 中。

#### TCG Software Stack

(term_tcg_software_stack)=

可信软件栈 [TCG](@tcg) Software Stack

为操作系统和应用软件提供使用 [TPM](@tpm) 的接口

### Threshold Signature Scheme

(term_threshold_signature_scheme)=

门限签名方案，将私钥拆分为 N 份，只要其中 M 份同意，
就可以生成签名。

### TTM

(ttm)=

Translation Table Manager

[DRM](@drm) 的首款内存管理器，试图实现大一统的内存管理，支持各类异构架构，所以相对较为复杂。

### TTP

(ttp)=

可信第三方，Trusted Third Party

### TVM

(tvm)=

TEE VM

见 [CVM](@cvm)。

## U

(term_u)=

### U2F

(u2f)=

Universal 2nd Factor

- <https://en.wikipedia.org/wiki/Universal_2nd_Factor>

### UAF

(uaf)=

Universal Authentication Framework

侧重于 Passwordless，无须密码登录，如生物识别登录等。

### UDS

Unix Domain Socket

Unix 通过文件系统路径提供的 socket 服务，一般仅用于本机的跨进程通讯。

### UEBA

(ueba)=

User and Entity Behavior Analytics

### UEFI

(term_uefi)=

统一的可扩展固件接口，Unified Extensible Firmware Interface

- [UEFI 引导与 BIOS 引导在原理上有什么区别？](https://www.zhihu.com/question/21672895)

取代 BIOS 的启动程序。
内置了大厂商公钥，对启动的 OS 会进行校验，拒绝不可信的 OS。

若是想要启动自定义的 OS，需要用自签的公私钥为 OS 签名，并将自签证书作为 [MOK](@term_uefi_mok)。

### UEFI MOK

(term_uefi_mok)=

UEFI Machine Owner Key

- [Machine Owner Key (MOK)](https://edk2-docs.gitbook.io/understanding-the-uefi-secure-boot-chain/additional_secure_boot_chain_implementations/machine_owner_key_mok)

![mok](https://s3.laisky.com/uploads/2022/08/mok.png)

### UKI

Systemd Unified Kernel Image

- [systemd v252 启用的 新功能](https://github.com/systemd/systemd/releases/tag/v252)
- [systemd-measure](<https://www.freedesktop.org/software/systemd/man/systemd-measure.html#:~:text=systemd%2Dmeasure%20is%20a%20tool,(7)%20is%20booted%20up.>)

### UMA

(uma)=

统一内存架构 Unified Memory Architecture

最早是由 [AMD APU](@amd_apu) 所提出。
一般指将多个异构芯片的内存统一到统一内存池和地址，加速访问。

![uma](https://s3.laisky.com/uploads/2022/09/uma.jpg)

和 [CUDA UVA](@cuda_uva) 的区别在于，UVA 仅统一了虚拟内存地址，而 UMA 是统合了物理内存。

### UMS

(ums)=

User Mode Setting

用户态运行的 [MS](@mode_settings)

### USNO

(usno)=

US Naval Observatory

负责根据原子钟为 GPS 系统提供时间的组织，全球的 NTP 服务器大多都会从 GPS 信号中获取时间。

## V

(term_v)=

### VA

(term_va)=

虚拟内存地址, Virtual memory Address

也称为 `linear address space`。

虚拟内存地址是 kernel 为每一个进程建立的抽象地址空间，
由 Page 构成，当进程试图读写页时会触发 #PF，kernel/[MMU](@mmu) 会加载[物理内存](@term_pa)。

也称为：

- [HVA](@term_host_virtual_addr)

### vDSO

(term_vdso)=

为了解决静态分配的安全问题而实现的动态 [vsyscall](@term_vsyscall)。

让一些 [syscall](@term_syscall) 不需要 trap 进内核就能直接在用户态返回，减少切换开销。

### VMM

(term_vmm)=

虚拟机管理器，Virtual Machine Manager

其他称谓：

- [hypervisor](@term_hypervisor)
- [Virtual Machine Monitor](@term_intel_vmm)

负责管理 guest os 的软件。

比较主流的 VMM 有：

- XEN & Qemu
- KVM & Qemu
- VMware
- Hyper-V

### VNF

(vnf)=

虚拟网元，Virtual Network Function

在云原生时代，各种虚拟网元取代硬件网络设备，支撑起云端复杂的网络拓扑

### VPWG

(vpwg)=

Virtualized Platform Working Group

### vsyscall

(term_vsyscall)=

- [c - What are vdso and vsyscall? - Stack Overflow](https://stackoverflow.com/questions/19938324/what-are-vdso-and-vsyscall/19942352#19942352)

kernel 会将 [syscall](@term_syscall) 地址映射到 userspace 内固定地址的一页上，因为空间有限，仅能放入 4 个 syscall，称为 vsyscall。

放入了四个常用的只读 syscall 来加速（clock_gettime 等），这些 syscall 不需要进入内核即可返回。

用户态程序可以通过固定的地址直接调用这些接口。

但是静态地址导致了安全问题（内存地址最好要是动态不可预测的），
所以为了安全，vsyscall 的固定地址被换成了 syscall trap 号，换句话说，本来为了不进入 kernel 的 syscall 实际上最后全部又被 kernel 接管了。

后来引入了动态链接的 [vDSO](@term_vdso) 彻底解决这一问题，vDSO 在用户态内存地址上随机分配 vsyscall，也突破了一页的限制，可以支持任意多的 vsyscall。

### vTPM

(vtpm)=

virtual TPM

TPM 虚拟化

- [QEMU TPM Device](https://qemu.readthedocs.io/en/latest/specs/tpm.html)

QEMU 的 vTPM 介绍。

- [Virtual Trusted Platform Module for Shielded VMs: security in plaintext](https://cloud.google.com/blog/products/identity-security/virtual-trusted-platform-module-for-shielded-vms-security-in-plaintext)

在 GCP 的这篇文章中，称 vTPM 之所以安全，是因为其运行于 Host 内存，而 VM 无法访问 😓。

## W

(term_w)=

### W3C

(w3c)=

World Wide Web Consortium

### W3C WebAuthn

(webauthn)=

W3C Web Authentication

- <https://webauthn.guide/>

## X

(term_x)=

### X.509

- X.509 v3 Certificate
- X.509 v2 [CRL](@term_crl)

## Y

(term_y)=

### Yubikey

(yubikey)=

Yubico 公司推出的便携式[加密固件](@hka)。

[Read More...](@yubikey_desc)

## Z

(term_z)=

### ZKP

(zkp)=

零知识证明 Zero—Knowledge Proof

由 S.Goldwasser、S.Micali 及 C.Rackoff 在 20 世纪 80 年代初提出的。
它指的是证明者能够在不向验证者提供任何有用的信息的情况下，使验证者相信某个论断是正确的。

两个参与者：证明者（Prover）和验证者（Verifier）。

Prover 持有 witness，Verifier 向 Prover 提出 challenge，Prover 根据 challenge 和 wintness 计算 statement，Verifier 根据 statement 判断 Prover 是否持有 witness。

传统 ZKP 需要双方多次交互，因为 Verifier 需要通过多次发送不同的 challenge 来降低 Prover 侥幸猜对的概率。而 [NIZK](@nizk) 允许双方仅交互一次。

### ZTN

(ztn)=

零信任网络, Zero Trust Network

打破过去的网络分区防护理念，不再执着于基于准入准出规则的边界防护，而是改为利用规则引擎，对所有的流量进行动态信任评分的机制。

---

[0-9](@term_09) | [A](@term_a) | [B](@term_b) | [C](@term_c) | [D](@term_d) | [E](@term_e) | [F](@term_f) | [G](@term_g) | [H](@term_h) | [I](@term_i) | [J](@term_j) | [K](@term_k) | [L](@term_l) | [M](@term_m) | [N](@term_n) | [O](@term_o) | [P](@term_p) | [Q](@term_q) | [R](@term_r) | [S](@term_s) | [T](@term_t) | [U](@term_u) | [V](@term_v) | [W](@term_w) | [X](@term_x) | [Y](@term_y) | [Z](@term_z)

---
