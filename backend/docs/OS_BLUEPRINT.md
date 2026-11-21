# MahaDevan's OS --- Master Project Blueprint

**Project name:** MahaDevan's OS\
**Base distribution:** Arch Linux\
**Architecture:** x86_64\
**Primary purpose:** Personal daily-driver Linux distribution,
development, gaming, AI/ML, and learning Linux system engineering\
**Long-term goal:** A maintainable, installable, publicly distributable
Linux distribution\
**Document purpose:** Master specification and phased instruction set
for an AI coding agent (Claude Code, Cursor, Codex, or equivalent)

------------------------------------------------------------------------

## 1. Project mission

Build **MahaDevan's OS**, a real Arch-based Linux distribution with a
distinctive, modern Wayland desktop experience inspired by COSMIC and
Hyprland.

This must be a functioning operating system distribution, not a mock
desktop, simulated OS, web-only dashboard, or collection of screenshots.
It must boot from a real ISO, run real Linux services, install onto real
storage, manage real packages, use actual GPU acceleration, and provide
working system recovery.

The first goal is a reliable personal daily-driver system. Public
distribution is a later goal and must follow reproducible builds,
hardware testing, documentation, security review, and a public beta.

### Non-negotiable principles

1.  Build incrementally. Each phase must work and pass its acceptance
    tests before the next phase is treated as complete.
2.  Reuse mature Linux components. Do not rewrite the Linux kernel,
    systemd, pacman, Hyprland, NetworkManager, PipeWire, or other
    foundational infrastructure.
3.  No fake functionality. No placeholder buttons, simulated system
    metrics, fake package operations, static demo data presented as live
    data, or controls that do nothing.
4.  Every UI control must call a real supported system API, service,
    command, or configuration workflow and must show errors honestly.
5.  Never run destructive disk, partition, bootloader, encryption, or
    host-system commands without explicit human approval.
6.  Do not overwrite or destabilize the developer's working operating
    system. Use a dedicated project directory, isolated build
    environments, and virtual machines.
7.  Prefer small, auditable components and documented interfaces over
    one large application.
8.  Keep the ISO reproducible and the package set versioned.
9.  Do not claim hardware compatibility until it has been tested on
    representative hardware.
10. Document design decisions, commands, dependencies, known
    limitations, and recovery procedures.

------------------------------------------------------------------------

## 2. Confirmed product requirements

### 2.1 Identity and audience

-   Name: **MahaDevan's OS**
-   Initial audience: the developer, for personal daily use.
-   Long-term audience: general x86_64 desktop and laptop users.
-   Main workloads:
    -   Daily desktop use
    -   Programming and software development
    -   Gaming
    -   AI and machine learning
    -   Linux and operating-system learning

### 2.2 Base system

  -----------------------------------------------------------------------
  Component                           Decision
  ----------------------------------- -----------------------------------
  Base                                Arch Linux

  Architecture                        x86_64

  Init and service manager            systemd

  Default kernel                      Linux stable

  Optional kernel                     Linux Zen / performance kernel

  Bootloader                          systemd-boot

  Default filesystem                  Btrfs

  Snapshots                           Btrfs snapshot integration

  Package manager                     pacman

  Additional package sources          AUR and official MahaDevan's
                                      repository

  Audio                               PipeWire

  Network                             NetworkManager

  Bluetooth                           BlueZ

  Login/display manager               SDDM

  Desktop session                     Wayland

  Compositor                          Hyprland

  Desktop shell                       Quickshell

  GPU rendering                       Hardware accelerated

  Driver policy                       Open-source drivers by default;
                                      proprietary options where required
  -----------------------------------------------------------------------

The system must support UEFI systems. Legacy BIOS support is not a
launch requirement unless it can be added without compromising the
primary boot design.

### 2.3 Desktop and user experience

Design direction: **COSMIC-inspired clarity combined with Hyprland's
dynamic tiling and motion**.

-   Dynamic tiling window management.
-   Smooth, configurable animations.
-   Keyboard and mouse controls.
-   Dynamic workspaces and workspace overview.
-   A top panel only.
-   Rofi-style application launcher.
-   Notification center.
-   Quick settings popup.
-   Clipboard manager.
-   Screenshot and screen recording tools.
-   Lock screen.
-   Wallpaper manager.

Desktop implementation: - Hyprland is the actual Wayland compositor. -
Quickshell is the shell framework for panel, launcher, overview,
notifications, quick settings, and related desktop surfaces. - Do not
build a new compositor in the initial project. - Keep shell
configuration and components modular.

### 2.4 File manager

Use **customized Dolphin**, not a new file manager.

Required features: - Dual-pane support. - Tabs. - File previews. -
Archive extraction. - Network locations. - Disk usage visualization. -
Right-click context menus. - Git integration. - Built-in terminal
integration.

Use Dolphin's existing capabilities and supported
extensions/configuration. Do not fork it unnecessarily. Any custom
patches must be isolated, documented, and maintainable.

### 2.5 Terminal

Use **Kitty** with MahaDevan's theme and configuration.

Required: - Split panes. - Multiple tabs. - GPU-accelerated rendering. -
Custom themes. - SSH integration. - Command search and history. - Custom
keyboard shortcuts. - Command-output search.

Use Kitty's actual configuration and capabilities. Do not create a fake
terminal UI.

### 2.6 Settings application

Build a native settings application using **Rust + GTK4 + Libadwaita**.

Required settings areas: - Display and resolution. - Keyboard and
mouse. - Hyprland configuration. - Appearance and themes. - Network and
Wi-Fi. - Bluetooth. - Audio devices. - Power and battery. - Users and
accounts. - System updates. - Storage and partitions. - Security and
firewall. - Drivers and GPU. - Startup applications. - Default
applications.

Advanced areas: - Window rules and animations. - Workspace
customization. - Advanced kernel settings. - Btrfs snapshot
management. - Developer options.

The application must use appropriate system services and APIs. It must
not directly edit privileged system files from an unprivileged GUI
process. Use narrowly scoped privileged helpers or established system
services where necessary. Validate configuration before applying it and
provide rollback or recovery guidance for risky changes.

### 2.7 Software store

Build a custom graphical software store using **Rust + GTK4 +
Libadwaita**.

Sources: - Official MahaDevan's repository. - Arch official
repositories. - Flatpak / Flathub. - AUR, with explicit warnings and
review.

Requirements: - Real package search, metadata, install, update, and
removal. - Clear source labels. - Show whether a package comes from
official repositories, Flatpak, or AUR. - Explain that AUR packages are
community-maintained build recipes, not official Arch packages. -
Require confirmation before installation/removal and before privileged
operations. - Display progress, logs, failures, and recovery
information. - Do not run arbitrary AUR build scripts silently or as
root. - Never present a package as installed until the package manager
confirms it. - Use pacman/libalpm-compatible workflows and Flatpak's
supported interfaces. Avoid concurrent package-manager transactions.

### 2.8 System monitor

Build a real system monitor with: - CPU usage and temperature. - GPU
usage and temperature. - RAM and swap. - Disk and NVMe health. - Network
traffic. - Process management. - Fan speeds and power consumption.

Hardware sensors may be unavailable on some systems. Show "not
available" or a clear permission/driver explanation instead of
fabricated values. Process termination must require user intent and
appropriate permission. NVMe health should use supported
tools/interfaces and should not imply that SMART data is a full
diagnostic guarantee.

### 2.9 Application technology

-   Native applications: **Rust + GTK4 + Libadwaita**.
-   Desktop shell: **Quickshell**, which uses Qt/QML.
-   Compositor: **Hyprland**.
-   File manager: customized Dolphin.
-   Terminal: Kitty.

These technologies intentionally coexist. Do not attempt to force
Quickshell into GTK or replace Hyprland with a custom compositor.

------------------------------------------------------------------------

## 3. Gaming, graphics, performance, security, and AI

### 3.1 Gaming

Balanced gaming setup: - Steam. - Proton. - Lutris. - Heroic Games
Launcher. - GameMode. - MangoHud. - Wine and Proton utilities.

Do not bundle copyrighted games or proprietary game assets. Provide
installation/configuration support and make optional components clear.
Test actual game launch and overlay behavior where feasible.

### 3.2 Graphics and GPU

Target AMD and NVIDIA systems.

AMD: - Mesa. - Vulkan support. - Kernel `amdgpu` driver where
supported. - Hardware acceleration.

NVIDIA: - Provide a documented supported driver-selection path. -
Support appropriate proprietary and open kernel module options based on
GPU generation and upstream driver support. - Handle initramfs and
kernel module configuration correctly. - Test Wayland behavior and
document limitations.

General: - GPU driver detection. - GPU monitoring. - OpenGL and Vulkan
support. - GPU switching only on hardware that supports it. - Optional
performance profiles.

Never assume one GPU configuration works on every device. Keep driver
installation modular and recoverable. Avoid installing both conflicting
driver stacks blindly.

### 3.3 Performance profiles

Provide: - Balanced mode. - Performance mode. - Power Saver mode. -
Automatic profile selection based on workload/power state. - Manual
override. - CPU frequency/governor controls where supported. - Battery
optimization. - Gaming profile. - Thermal monitoring. - Startup
application management. - Optional zram.

Use established tools and kernel interfaces where possible. Never force
unsafe CPU/GPU overclocking or thermal limits. Profile changes must be
reversible and report when hardware does not support a requested
setting.

### 3.4 Security and privacy

Required: - Firewall enabled by default with a sensible default
policy. - Secure password authentication. - Secure Boot support. - LUKS
full-disk encryption option during installation. - Automatic
security-update notifications. - Flatpak sandboxing. - Secure login and
screen locking. - SSH security configuration guidance. - Optional audit
logs. - USB device security controls where feasible.

Secure Boot should be supported, not universally required. Document key
enrollment, signing, and recovery implications. Do not claim Secure Boot
works unless the complete boot chain has been tested.

Security controls must not lock users out without recovery
documentation. Do not enable unattended destructive upgrades. Users must
be able to inspect update details and control installation.

### 3.5 AI and machine learning

AI is **optional**, powered locally by Ollama when installed.

Required: - Natural-language system assistance. - Explain terminal
commands. - Local model management. - Developer coding assistant
integration.

The initial AI scope is developer-oriented, not a mandatory AI desktop
layer.

Safety: - AI-generated commands are suggestions, not trusted
instructions. - Explain commands and identify potentially destructive
operations. - Never execute privileged commands without explicit user
confirmation. - Never run commands from model output automatically. -
Show the exact command before execution. - Make local model downloads
optional and show disk-space requirements. - Do not bundle large model
weights in the ISO. - Do not claim GPU acceleration unless the selected
backend and hardware are actually supported.

AMD and NVIDIA acceleration paths differ. Treat ROCm, CUDA, Vulkan, and
CPU inference as separate capability paths. Detect capabilities rather
than promising universal acceleration.

### 3.6 Development and virtualization tools

Provide packages or install profiles for: - Docker and Docker Compose. -
KVM/QEMU. - Virt-Manager. - Libvirt. - Podman. - Git and GitHub CLI. -
Python. - Node.js and npm. - Rust toolchain. - Java and Maven/Gradle. -
VS Code or compatible editor. - Android development tools as optional
packages.

Do not force every large development tool onto every installation. Use
sensible package groups/profiles and let the user choose.

### 3.7 Customization

Initial scope: **moderate customization**: - Themes. - Wallpapers. -
Icons. - Fonts.

Keep the design coherent and avoid a sprawling plugin ecosystem in the
first release. Advanced customization can be considered after the core
desktop is stable.

------------------------------------------------------------------------

## 4. Installer, live environment, ISO, and release

### 4.1 Installer

Customize **Calamares** initially. Do not build a custom installer from
scratch in the first release.

Required: - Automatic partitioning. - Manual/advanced partitioning. -
Btrfs filesystem. - Optional LUKS encryption. - Dual-boot installation
alongside Windows where safely supported. - Bootloader configuration. -
User account creation. - Timezone selection. - Keyboard selection. -
Hardware and driver detection.

Installer safety: - Clearly display selected target disks and
partitions. - Explain destructive operations. - Require explicit
confirmation before formatting or deleting partitions. - Re-check target
devices immediately before destructive operations. - Handle installer
failure without claiming success. - Preserve existing EFI System
Partitions and other operating systems when the selected layout requires
it. - Never assume disk names such as `/dev/sda` or `/dev/nvme0n1`. -
Test UEFI and dual-boot behavior in disposable VMs before physical use.

### 4.2 Live USB

Provide a full live desktop with: - MahaDevan's Hyprland/Quickshell
session. - Basic system utilities. - Network, audio, and graphics test
capability. - Calamares installer. - Clear live-session indicator and
installation guidance.

The live session should allow users to test Wi-Fi, sound, graphics,
display scaling, and basic peripherals before installation.

### 4.3 ISO size

Target a standard ISO of approximately **3--5 GB**, subject to actual
package contents and compression.

Do not include large Ollama models, games, or optional development
stacks in the base ISO. Provide installation profiles and post-install
setup instead. Measure the actual artifact size; the target is not a
reason to remove essential reliability components.

### 4.4 Recovery

Required: - Automatic Btrfs snapshots before system updates. - Bootable
snapshot rollback workflow. - Recovery mode from boot menu. - Bootloader
repair option. - Restore system configuration. - Create and restore
backups. - GUI update manager. - Terminal package-management support.

Important: - Btrfs snapshots are not backups. - Snapshot layout and boot
integration must be designed and tested, not assumed. - Use an
established snapshot tool and pacman hook integration where
appropriate. - Ensure snapshots include the correct subvolumes and
exclude volatile data as intended. - Provide a recovery path if the root
filesystem cannot boot. - Do not automatically delete the only
known-good recovery point. - Test rollback after failed kernel, driver,
and system updates.

### 4.5 Branding

Provide: - Custom logo and icon set. - Boot splash. - Login screen. -
Wallpaper collection. - systemd-boot branding/theme where technically
supported. - Branded terminal and desktop themes. - Documentation and
official website plan. - Official package repository plan.

Branding must not compromise boot reliability, accessibility,
readability, or system diagnostics.

### 4.6 Release strategy

Release progression: 1. Personal development builds. 2. Automated and VM
testing. 3. Physical hardware testing. 4. Internal alpha. 5. Public
beta. 6. Stable release only after defined quality gates.

Do not announce a stable release merely because an ISO boots once.

------------------------------------------------------------------------

## 5. Development environment and workflow

### 5.1 Development approach

Use **incremental development**.

Develop on the developer's existing Linux installation in a dedicated
project directory, while using an Arch Linux VM for isolated builds and
destructive installation tests.

Never let the agent: - Repartition the developer's real disk. - Reformat
the host filesystem. - Replace the host bootloader. - Change host
firewall/network configuration without approval. - Install experimental
drivers on the host without approval. - Run unreviewed root scripts on
the host.

### 5.2 Repository structure

Use this modular starting structure:

``` text
mahadevans-os/
├── README.md
├── LICENSE
├── CONTRIBUTING.md
├── SECURITY.md
├── CHANGELOG.md
├── branding/
│   ├── logos/
│   ├── icons/
│   ├── wallpapers/
│   ├── boot/
│   └── themes/
├── packages/
│   ├── base/
│   ├── desktop/
│   ├── gaming/
│   ├── development/
│   ├── ai/
│   └── optional/
├── configs/
│   ├── systemd/
│   ├── pacman/
│   ├── network/
│   ├── pipewire/
│   ├── sddm/
│   └── security/
├── desktop/
│   ├── hyprland/
│   ├── quickshell/
│   ├── themes/
│   ├── launcher/
│   └── session/
├── applications/
│   ├── settings/
│   ├── software-store/
│   ├── system-monitor/
│   └── shared/
├── installer/
│   ├── calamares/
│   ├── partitioning/
│   └── recovery/
├── iso/
│   ├── profile/
│   ├── scripts/
│   └── checks/
├── repository/
│   ├── packaging/
│   └── signing/
├── scripts/
│   ├── development/
│   ├── build/
│   └── maintenance/
├── tests/
│   ├── unit/
│   ├── integration/
│   ├── vm/
│   ├── installer/
│   └── hardware/
└── documentation/
    ├── architecture/
    ├── installation/
    ├── recovery/
    ├── development/
    └── release/
```

The agent may add files and subdirectories when needed, but must
preserve clear separation of concerns. Keep application source code,
package recipes, ISO profiles, system configuration, and generated
artifacts separate.

### 5.3 Source control and reproducibility

-   Use Git from the first day.
-   Commit small, coherent changes.
-   Use feature branches for risky work.
-   Never commit secrets, signing keys, tokens, passwords, private SSH
    keys, or personal configuration.
-   Include `.gitignore` entries for `.env`, virtual environments, build
    directories, caches, generated ISOs, VM disks, and local secrets.
-   Provide example configuration files without secrets.
-   Pin or record package versions and build inputs where practical.
-   Keep build scripts idempotent where possible.
-   Generate build manifests and checksums for ISO artifacts.
-   Sign official repository packages and release artifacts before
    public distribution.
-   Document how to reproduce a build from a clean Arch build
    environment.

------------------------------------------------------------------------

## 6. Implementation phases and coding-agent prompts

The agent must work one phase at a time. At the start of each phase,
inspect the repository, report current state, identify prerequisites,
and propose a short implementation plan. Do not silently skip failed
acceptance tests.

### Phase 1 --- Arch base system and reproducible ISO foundation

**Goal:** Establish the real Arch-based build pipeline and a minimal
bootable image.

Tasks: 1. Initialize the repository and documentation. 2. Choose and
document the Arch ISO build approach (for example, archiso). 3. Create a
minimal MahaDevan's ISO profile. 4. Define package groups and system
configuration. 5. Configure systemd, stable kernel, systemd-boot, UEFI
boot, networking, and basic utilities. 6. Define Btrfs subvolume and
mount strategy for installation. 7. Add build scripts that run in an
isolated Arch VM/container/build environment. 8. Generate ISO checksums
and a manifest. 9. Document the build process and known limitations.

Acceptance tests: - ISO builds reproducibly from documented steps. - ISO
boots in a UEFI VM. - Live environment reaches a usable shell/session. -
Network can be configured. - The build does not alter the host disk or
bootloader. - Build logs and artifact checksums are saved.

**Agent prompt:**

> Implement Phase 1 only. Build a real Arch-based ISO using a
> documented, reproducible Arch-supported build process. Do not build
> the full desktop yet. Work only inside the project directory and
> isolated build environment. Do not modify host partitions, bootloader,
> firewall, or system configuration. Produce the ISO profile, package
> lists, scripts, build manifest, checksums, documentation, and tests.
> Run the build and UEFI VM boot test. Report exact commands, outputs,
> failures, and remaining limitations. Do not claim success unless the
> artifact boots.

### Phase 2 --- Hyprland and Quickshell desktop

**Goal:** Deliver a real usable Wayland desktop session.

Tasks: 1. Package Hyprland and required Wayland components. 2. Configure
SDDM to offer the MahaDevan's session. 3. Create modular Hyprland
configuration. 4. Integrate Quickshell. 5. Build the top panel,
launcher, workspace overview, notifications, quick settings, clipboard,
screenshot/recording controls, lock screen, and wallpaper manager. 6.
Add keyboard and mouse controls. 7. Provide sensible fallback behavior
if a shell component fails. 8. Add theme and wallpaper configuration. 9.
Document all keybindings and configuration paths.

Acceptance tests: - SDDM launches the session. - Hyprland starts as the
actual compositor. - Quickshell components render and respond. - Apps
can be launched and managed. - Workspaces and tiling work. -
Notifications and quick settings connect to real system services. -
Session logs are available for troubleshooting. - A shell failure does
not make the system unrecoverable.

**Agent prompt:**

> Implement Phase 2 on top of the working Phase 1 image. Use Hyprland as
> the actual compositor and Quickshell for desktop shell components. Do
> not write a compositor. Every panel item and control must read or
> change real system state. Keep shell components modular and
> restartable. Test login, app launching, tiling, workspaces,
> notifications, audio/network quick settings, screenshot, lock, and
> recovery from a failed shell component. Update the ISO profile and
> documentation only after tests pass.

### Phase 3 --- Native applications and desktop tools

**Goal:** Deliver useful, working applications.

Tasks: 1. Customize Dolphin and configure its required features. 2.
Configure Kitty with MahaDevan's theme, tabs, splits, SSH, history,
shortcuts, and output search. 3. Build the Rust/GTK4/Libadwaita settings
application. 4. Build the Rust/GTK4/Libadwaita software store. 5. Build
the Rust/GTK4/Libadwaita system monitor. 6. Define shared UI style,
error handling, logging, settings storage, and IPC conventions. 7.
Package applications cleanly.

Acceptance tests: - Dolphin features work using actual file
operations. - Kitty launches and its configuration is applied. -
Settings app reads and changes actual settings. - Privileged operations
use a safe authorization boundary. - Store can search and install a test
package in a disposable VM. - Store correctly handles failures and
package-manager locks. - System monitor reads actual metrics and reports
unavailable sensors honestly. - Applications can be built from
documented source instructions.

**Agent prompt:**

> Implement Phase 3 as separate, maintainable applications. Use Rust,
> GTK4, and Libadwaita for new native applications. Customize Dolphin
> and Kitty rather than replacing them. Do not display invented metrics
> or fake package results. Use supported system APIs, D-Bus services,
> package-manager interfaces, and least-privilege helpers. Add unit and
> integration tests. Test package changes only in a disposable VM.
> Document every privileged action and its authorization model.

### Phase 4 --- Gaming, drivers, performance, security, AI, and development

**Goal:** Add optional, testable workload profiles.

Tasks: 1. Create gaming package group and setup documentation. 2. Add
AMD and NVIDIA driver selection/detection logic with safe, documented
paths. 3. Integrate Vulkan/OpenGL and GPU monitoring. 4. Add
balanced/performance/power-saver profiles and safe automatic switching.
5. Configure firewall defaults and security notifications. 6. Add Secure
Boot support documentation and test plan. 7. Integrate optional LUKS
installation capability. 8. Add optional Ollama installation/model
manager integration. 9. Add AI command explanation with mandatory user
confirmation before execution. 10. Add development and virtualization
package groups. 11. Test KVM/libvirt, Docker/Podman, and permissions.
12. Add hardware capability detection and clear unsupported-feature
messages.

Acceptance tests: - Gaming tools install and launch in a VM or supported
test machine. - GPU detection identifies actual hardware and driver
status. - Vulkan checks report actual capability. - Performance profiles
change supported settings and can be reversed. - Firewall is active with
documented defaults. - AI does not execute commands automatically. -
Ollama is optional and model downloads are not included in the ISO. -
Virtualization checks report hardware and permission requirements. - No
driver path is advertised as tested without a corresponding test record.

**Agent prompt:**

> Implement Phase 4 as optional package groups and carefully scoped
> system integrations. Support AMD and NVIDIA through distinct,
> documented driver paths. Never install conflicting GPU stacks blindly.
> Implement real performance profiles with safe rollback. Keep Ollama
> and large models optional. AI output must never execute privileged
> commands automatically. Add tests for firewall state, GPU capability
> detection, package groups, virtualization readiness, and reversible
> profile changes. Document hardware-specific limitations.

### Phase 5 --- Calamares installer, Btrfs snapshots, and recovery

**Goal:** Make the distribution safely installable and recoverable.

Tasks: 1. Customize Calamares branding and configuration. 2. Define
supported UEFI partition layouts. 3. Implement automatic and manual
partitioning. 4. Add optional LUKS encryption. 5. Add dual-boot
detection and safe handling. 6. Create Btrfs subvolume layout and mount
configuration. 7. Configure systemd-boot installation. 8. Configure user
creation, locale, timezone, keyboard, and network setup. 9. Integrate
snapshot creation before package updates. 10. Provide bootable rollback
and recovery workflows. 11. Add bootloader repair and configuration
restoration. 12. Document external backup and restore procedures.

Acceptance tests: - Install to a disposable UEFI VM disk. - Test
automatic and manual partitioning. - Test encrypted and unencrypted
installation. - Test dual boot using a disposable Windows VM image where
feasible. - Confirm existing partitions are not touched outside the
user's selected plan. - Boot the installed system. - Create a snapshot,
perform a controlled change, and roll back. - Test recovery after a
deliberately broken test configuration. - Confirm the installer requires
explicit approval for destructive operations.

**Agent prompt:**

> Implement Phase 5 only after Phases 1--4 have stable test builds.
> Customize Calamares and implement real partitioning, Btrfs, optional
> LUKS, systemd-boot, user setup, snapshots, and recovery. All
> destructive operations must show the exact target device and require
> explicit confirmation. Never run installer tests against the
> developer's real disk. Use disposable VM disks and automated test
> cases. Treat snapshots and external backups as different features.
> Demonstrate a successful install, first boot, snapshot, rollback, and
> recovery before declaring completion.

### Phase 6 --- Full ISO integration and quality assurance

**Goal:** Produce a release-candidate ISO.

Tasks: 1. Integrate all approved package groups and configurations. 2.
Ensure the live desktop and installer work together. 3. Verify package
dependencies and conflicts. 4. Verify boot paths and systemd services.
5. Test AMD and NVIDIA paths on representative hardware where available.
6. Test Wi-Fi, Bluetooth, audio, display, suspend/resume, and battery
behavior. 7. Test gaming and development profiles. 8. Test upgrades,
failed updates, snapshots, and rollback. 9. Run security and dependency
checks. 10. Measure ISO size and boot/install times. 11. Generate
release notes, checksums, manifests, and known-issues list.

Acceptance tests: - ISO builds from a clean environment. - Live USB
boots on supported UEFI hardware. - Installer completes in a VM. -
Installed OS boots and logs in. - Core desktop applications work. -
Network, audio, and GPU functionality are tested and recorded. -
Snapshot rollback and recovery pass. - No critical known issue remains
hidden. - Release artifacts include checksums and build metadata.

**Agent prompt:**

> Integrate the completed phases into a release-candidate ISO. Do not
> add new features during final integration unless they fix a blocker.
> Run the complete test matrix in clean VMs and available physical
> hardware. Record exact hardware, driver versions, kernel, test steps,
> results, and failures. Produce ISO, checksum, package manifest,
> release notes, known issues, and reproducible build instructions. Do
> not label it stable if any critical installation, boot, recovery, or
> security test fails.

### Phase 7 --- Public beta and distribution

**Goal:** Prepare a responsible public beta.

Tasks: 1. Create release channels and versioning policy. 2. Establish
package signing and repository key management. 3. Publish repository
metadata and package signing instructions. 4. Create official website
and documentation structure. 5. Publish installation, upgrade, rollback,
and recovery guides. 6. Publish hardware compatibility and known-issues
pages. 7. Create issue templates and contribution guidelines. 8.
Establish security vulnerability reporting. 9. Publish ISO checksums and
release signatures. 10. Define support expectations and release cadence.

Acceptance tests: - A clean user can verify the ISO
checksum/signature. - A clean user can install using public
documentation. - Package repository signatures are verified. - Update
and rollback instructions work. - Known issues are visible. - No private
signing key or secret is included in source control or ISO. - Public
beta is clearly identified as beta.

**Agent prompt:**

> Prepare a public beta release, not an unsupported claim of production
> maturity. Add versioning, signed repository/release artifacts,
> documentation, installation and recovery guides, issue templates,
> security reporting, and known issues. Review the repository for
> secrets and private keys. Verify the published ISO and instructions
> from a clean environment. Preserve a clear distinction between tested
> functionality, experimental functionality, and planned functionality.

------------------------------------------------------------------------

## 7. System architecture and integration rules

### 7.1 Layered architecture

``` text
User applications
  ├── Customized Dolphin
  ├── Kitty
  ├── MahaDevan's Settings (Rust / GTK4)
  ├── MahaDevan's Store (Rust / GTK4)
  └── MahaDevan's System Monitor (Rust / GTK4)

Desktop shell
  └── Quickshell
       ├── Top panel
       ├── Launcher
       ├── Overview
       ├── Notifications
       ├── Quick settings
       ├── Clipboard
       ├── Screenshot / recording
       ├── Lock screen integration
       └── Wallpaper manager

Compositor
  └── Hyprland (Wayland)

System integration
  ├── systemd / D-Bus
  ├── NetworkManager
  ├── PipeWire
  ├── BlueZ
  ├── polkit
  ├── UPower / power services
  ├── pacman / libalpm workflows
  ├── Flatpak
  └── Btrfs snapshot tooling

Arch Linux base
  ├── Linux stable kernel
  ├── Optional Zen kernel
  ├── systemd-boot
  ├── Btrfs
  └── Arch package ecosystem
```

### 7.2 Privilege boundary

-   Normal desktop applications run unprivileged.
-   Use polkit or established system services for authorized privileged
    actions.
-   Never embed passwords in scripts, source code, logs, or command
    arguments.
-   Avoid broad passwordless sudo rules.
-   Validate inputs at the boundary.
-   Use fixed, audited command arguments rather than interpolating
    arbitrary user text into shell commands.
-   Log security-relevant operations without logging secrets.
-   Require user confirmation for destructive or privileged actions.

### 7.3 Package management

-   Never run concurrent pacman transactions.
-   Coordinate updates through one update service/lock.
-   Clearly identify official, community, Flatpak, and custom repository
    sources.
-   Do not run AUR build scripts as root.
-   Sign official repository packages and repository metadata.
-   Keep repository signing keys private and outside the source
    repository.
-   Provide a documented key rotation and revocation plan before public
    release.

### 7.4 Configuration management

-   Keep default configuration in version control.
-   Separate system defaults from per-user settings.
-   Back up user configuration before migration.
-   Validate generated Hyprland and Quickshell configuration.
-   Provide a safe fallback session/configuration.
-   Do not overwrite user configuration silently during updates.

------------------------------------------------------------------------

## 8. Testing strategy and quality gates

### 8.1 Test environments

1.  Unit tests for Rust applications and scripts.
2.  Integration tests in an Arch VM.
3.  UEFI boot tests.
4.  Installer tests using disposable virtual disks.
5.  Snapshot and recovery tests.
6.  Physical hardware tests.
7.  Upgrade tests from the previous build.

### 8.2 Primary hardware target

The first physical test target is the developer's AMD laptop, with an
AMD Ryzen 5 5600H-class platform, integrated AMD graphics and Radeon RX
6500M-class discrete graphics. The system should also aim to support
broader x86_64 AMD and NVIDIA hardware.

Do not hardcode this machine's devices, disk names, Wi-Fi adapter, or
display configuration into the distribution. Detect hardware
dynamically.

### 8.3 Required test matrix

  Area             Required test
  ---------------- ------------------------------------------------------
  Boot             UEFI live boot and installed boot
  Installer        Automatic and manual install to disposable disk
  Encryption       LUKS install and unlock
  Filesystem       Btrfs subvolumes and mounts
  Recovery         Snapshot creation and rollback
  Boot repair      Recover a broken test boot configuration
  Desktop          SDDM, Hyprland, Quickshell
  Graphics         AMD and NVIDIA driver paths
  Rendering        Vulkan/OpenGL capability detection
  Network          Wi-Fi and Ethernet through NetworkManager
  Bluetooth        Device discovery and connection
  Audio            PipeWire input/output
  Power            Suspend/resume and battery reporting
  Gaming           Steam/Proton and overlay setup
  Packages         pacman, Flatpak, AUR warnings
  Security         Firewall and privilege boundaries
  AI               Ollama optional install and safe command explanation
  Virtualization   KVM/libvirt readiness
  Updates          Update, snapshot, failure handling, rollback

### 8.4 Definition of done

A feature is done only when: - It is implemented, not mocked. - Its
dependencies and limitations are documented. - It has appropriate
tests. - It handles failure states. - It is packaged or integrated into
the actual OS. - Its user-facing controls work. - Its acceptance
criteria pass. - Its status is accurately reported.

------------------------------------------------------------------------

## 9. Coding-agent operating protocol

At the beginning of each session:

1.  Read this blueprint and the repository README.
2.  Inspect the current branch, working tree, project structure, and
    latest test reports.
3.  Identify the active phase and its prerequisites.
4.  Report what is already implemented and what remains.
5.  Propose a short, concrete plan for the current task.
6.  Work only on the current phase unless explicitly asked otherwise.

During implementation: - Prefer small changes and readable code. -
Explain architecture choices briefly. - Do not replace working code
without understanding it. - Do not introduce unnecessary dependencies. -
Do not silently change project scope. - Do not use placeholder
implementations to claim progress. - Add tests with each meaningful
feature. - Keep documentation current. - Preserve user changes in the
working tree.

Before running commands: - Classify commands as read-only,
project-local, privileged, or destructive. - Ask for approval before
privileged or destructive host operations. - Use disposable VMs for
disk, bootloader, installer, and recovery tests. - Never run `mkfs`,
`wipefs`, partitioning tools, bootloader installation, or destructive
disk commands against an unknown target. - Never assume a disk
identifier. - Never expose secrets in terminal output or logs.

At the end of each task, report: 1. Files created or changed. 2.
Functionality implemented. 3. Commands run. 4. Tests passed and failed.
5. Known limitations. 6. Security or compatibility concerns. 7. Exact
next task. 8. Whether the current phase acceptance criteria are
satisfied.

### Master instruction to the coding agent

> You are the engineering agent for MahaDevan's OS, a real Arch-based
> Linux distribution. Treat this blueprint as the project specification.
> Build the distribution incrementally in the seven defined phases.
> Prioritize a reliable, maintainable system over visual polish or
> feature count. Use existing Linux infrastructure rather than
> reinventing it. Never simulate OS functionality, never claim untested
> compatibility, and never perform destructive host operations without
> explicit approval. Work in the repository and isolated VM/build
> environments. Each phase must pass its acceptance tests before being
> considered complete. Maintain documentation, tests, reproducible build
> instructions, and honest status reports. If a requirement is
> technically unsafe, unsupported, or too large for the current phase,
> explain the limitation and propose a safe staged alternative rather
> than implementing a fake version.

------------------------------------------------------------------------

## 10. Scope control and realistic priorities

This project is large. The first usable release should focus on: 1. A
bootable Arch-based ISO. 2. A reliable Hyprland + Quickshell desktop. 3.
Working networking, audio, login, and graphics. 4. Customized Dolphin
and Kitty. 5. Basic but real settings, store, and system monitor
applications. 6. Safe Calamares installation. 7. Btrfs snapshots and
tested recovery.

Gaming, AI, advanced GPU management, broad hardware support, and public
infrastructure should be added in controlled stages.

Do not make a custom kernel, custom compositor, custom package manager,
custom file manager, or custom installer a launch requirement. These
would dramatically increase maintenance and delay a usable distribution.

A public release also requires ongoing maintenance: kernel updates,
package rebuilds, security advisories, repository signing, hardware
regression tests, and clear support policies. A one-time ISO build is
not a maintained distribution.

------------------------------------------------------------------------

## 11. Initial project kickoff checklist

The first coding-agent task should be limited to repository inspection
and Phase 1 planning.

-   [ ] Create the project directory and Git repository.
-   [ ] Add this blueprint as `OS_BLUEPRINT.md`.
-   [ ] Create the initial repository structure.
-   [ ] Choose and document the ISO build method.
-   [ ] Create a minimal Arch ISO profile.
-   [ ] Set up an isolated Arch VM/build environment.
-   [ ] Build the first minimal ISO.
-   [ ] Boot it in a UEFI VM.
-   [ ] Save build logs, manifest, and checksum.
-   [ ] Review Phase 1 acceptance tests before adding the desktop.

**Do not start by implementing every desktop application. First prove
that the project can reliably build and boot a real Arch-based ISO.**

------------------------------------------------------------------------

## 12. Project success criteria

MahaDevan's OS succeeds when it is: - A real, reproducibly buildable
Arch-based distribution. - Bootable from USB on supported UEFI x86_64
hardware. - Installable through a safe graphical installer. - Usable as
a daily-driver Wayland desktop. - Built from maintainable, documented
components. - Able to update and recover from failed updates. - Honest
about hardware support and limitations. - Safe to test without risking
the developer's existing installation. - Ready for public beta only
after the complete release test plan passes.

**End of blueprint.**
