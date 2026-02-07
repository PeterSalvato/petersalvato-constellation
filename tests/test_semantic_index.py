from scripts.semantic_index import SemanticIndexer


# Tier 1: Protocols
def test_detect_aetherwright_mention():
    indexer = SemanticIndexer()
    chat = {
        "title": "Order of the Aetherwright structure",
        "content": "The ritual framework for sovereign cognition...",
        "timestamp": "2026-01-26T13:04:42.022Z"
    }

    projects = indexer.detect_projects(chat)

    assert "order-of-the-aetherwright" in projects
    assert projects["order-of-the-aetherwright"]["confidence"] == "high"


def test_detect_savepoint_keyword():
    indexer = SemanticIndexer()
    chat = {
        "title": "Thinking about turning points",
        "content": "I need to mark where my understanding shifted, like a savepoint in thinking...",
        "timestamp": "2026-01-26T13:04:42.022Z"
    }

    projects = indexer.detect_projects(chat)

    assert "savepoint-protocol" in projects
    assert projects["savepoint-protocol"]["confidence"] == "medium"


def test_detect_ai_devops_workbench():
    indexer = SemanticIndexer()
    chat = {
        "title": "Fighting vibecoding",
        "content": "We need to document architectural decisions to prevent AI agents from repeating mistakes...",
        "timestamp": "2026-01-26T13:04:42.022Z"
    }

    projects = indexer.detect_projects(chat)

    assert "ai-devops-workbench" in projects
    assert projects["ai-devops-workbench"]["confidence"] == "high"


def test_detect_portable_agency():
    indexer = SemanticIndexer()
    chat = {
        "title": "Self-discovering specialists",
        "content": "The portable agency detects your tech stack and automatically configures verification tools. Project manager, tech lead, frontend, backend specialists all included.",
        "timestamp": "2026-01-26T13:04:42.022Z"
    }

    projects = indexer.detect_projects(chat)

    assert "portable-agency" in projects
    assert projects["portable-agency"]["confidence"] == "high"


# Tier 2: Applied Systems
def test_detect_aiden_jae():
    indexer = SemanticIndexer()
    chat = {
        "title": "Luxury jewelry branding",
        "content": "Aiden Jae proves that luxury and organic can coexist. The tropical South Florida textures inform everything from logo to photography.",
        "timestamp": "2026-01-26T13:04:42.022Z"
    }

    projects = indexer.detect_projects(chat)

    assert "aiden-jae" in projects
    assert projects["aiden-jae"]["confidence"] == "high"


def test_detect_altrueism():
    indexer = SemanticIndexer()
    chat = {
        "title": "Brand remediation project",
        "content": "Altrueism is about fixing a brand. Taking a gaudy decorated apparel company and proving it can transition to handcrafted artisanal production through complete visual and tonal remediation.",
        "timestamp": "2026-01-26T13:04:42.022Z"
    }

    projects = indexer.detect_projects(chat)

    assert "altrueism" in projects
    assert projects["altrueism"]["confidence"] == "high"


def test_detect_everyday_gold():
    indexer = SemanticIndexer()
    chat = {
        "title": "Natural deodorant brand",
        "content": "Everyday Gold is a natural deodorant that lives under the Aiden Jae umbrella. Same brand philosophy, different product category.",
        "timestamp": "2026-01-26T13:04:42.022Z"
    }

    projects = indexer.detect_projects(chat)

    assert "everyday-gold" in projects
    assert projects["everyday-gold"]["confidence"] == "high"


def test_detect_encore():
    indexer = SemanticIndexer()
    chat = {
        "title": "Enterprise platform stewardship",
        "content": "Encore is 40,000+ users and 99.9% uptime. Windows Forms to web migration that has survived 12 years of stewardship at scale.",
        "timestamp": "2026-01-26T13:04:42.022Z"
    }

    projects = indexer.detect_projects(chat)

    assert "encore" in projects
    assert projects["encore"]["confidence"] == "high"


def test_detect_modernist_homestead():
    indexer = SemanticIndexer()
    chat = {
        "title": "Home system for neurodivergent needs",
        "content": "Modernist Homestead unifies cooking, horticulture, hydroponics, and mycology through neurodivergent scaffolding. A home system that works WITH how your brain operates.",
        "timestamp": "2026-01-26T13:04:42.022Z"
    }

    projects = indexer.detect_projects(chat)

    assert "modernist-homestead" in projects
    assert projects["modernist-homestead"]["confidence"] == "high"


# Tier 3: Practice
def test_detect_echo_and_bone():
    indexer = SemanticIndexer()
    chat = {
        "title": "Stoic philosophy poster series",
        "content": "Echo & Bone is three posters on Stoic philosophy. Engraving-style illustrations with black letter typography in a centered grid structure. Can philosophy be visual?",
        "timestamp": "2026-01-26T13:04:42.022Z"
    }

    projects = indexer.detect_projects(chat)

    assert "echo-and-bone" in projects
    assert projects["echo-and-bone"]["confidence"] == "high"


def test_detect_mathontape():
    indexer = SemanticIndexer()
    chat = {
        "title": "Electronic music branding",
        "content": "MathOnTape is retro-futuristic branding for electronic music. Cassette futurism and dot matrix typography prove that vintage aesthetics aren't nostalgia if chosen intentionally.",
        "timestamp": "2026-01-26T13:04:42.022Z"
    }

    projects = indexer.detect_projects(chat)

    assert "mathontape" in projects
    assert projects["mathontape"]["confidence"] == "high"


def test_detect_photogeography():
    indexer = SemanticIndexer()
    chat = {
        "title": "Grid systems with spatial data",
        "content": "Photogeography pairs central photographs with QR codes, location metadata, latitude and longitude. A poster series testing whether grid systems can elegantly hold geographical information.",
        "timestamp": "2026-01-26T13:04:42.022Z"
    }

    projects = indexer.detect_projects(chat)

    assert "photogeography" in projects
    assert projects["photogeography"]["confidence"] == "high"


def test_detect_versagrams():
    indexer = SemanticIndexer()
    chat = {
        "title": "Lyrics and AI art posters",
        "content": "Versagrams combines song lyrics with generative AI artwork in a grid system structure. Testing whether lyrics and AI visuals can encode meaning together through constraint.",
        "timestamp": "2026-01-26T13:04:42.022Z"
    }

    projects = indexer.detect_projects(chat)

    assert "versagrams" in projects
    assert projects["versagrams"]["confidence"] == "high"


def test_detect_the_deep_cuts():
    indexer = SemanticIndexer()
    chat = {
        "title": "DJ methodology book concept",
        "content": "The Deep Cuts is a book concept on DJ methodology for music appreciation. It's about how DJs curate and select music for deeper engagement.",
        "timestamp": "2026-01-26T13:04:42.022Z"
    }

    projects = indexer.detect_projects(chat)

    assert "the-deep-cuts" in projects
    assert projects["the-deep-cuts"]["confidence"] == "high"


def test_detect_cryptozoology():
    indexer = SemanticIndexer()
    chat = {
        "title": "Mythology research project",
        "content": "Cryptozoology explores how research methodology applies to mythology and legend.",
        "timestamp": "2026-01-26T13:04:42.022Z"
    }

    projects = indexer.detect_projects(chat)

    assert "cryptozoology" in projects
    assert projects["cryptozoology"]["confidence"] == "high"


def test_detect_monstrum():
    indexer = SemanticIndexer()
    chat = {
        "title": "Design and visual research",
        "content": "Monstrum is visual design experimentation.",
        "timestamp": "2026-01-26T13:04:42.022Z"
    }

    projects = indexer.detect_projects(chat)

    assert "monstrum" in projects
    assert projects["monstrum"]["confidence"] == "high"


def test_detect_motorology():
    indexer = SemanticIndexer()
    chat = {
        "title": "Automotive systems research",
        "content": "Motorology investigates automotive design and systems thinking.",
        "timestamp": "2026-01-26T13:04:42.022Z"
    }

    projects = indexer.detect_projects(chat)

    assert "motorology" in projects
    assert projects["motorology"]["confidence"] == "high"


def test_detect_everyday_gold_practice():
    indexer = SemanticIndexer()
    chat = {
        "title": "Product research for deodorant",
        "content": "Everyday Gold Practice is product research exploring deodorant formulation and design.",
        "timestamp": "2026-01-26T13:04:42.022Z"
    }

    projects = indexer.detect_projects(chat)

    assert "everyday-gold-practice" in projects
    assert projects["everyday-gold-practice"]["confidence"] == "high"
