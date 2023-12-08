export const load = () => {
    const experiences = async () => {
        return await fetch('http://localhost:8000/api/experiences/').then(res => res.json())
    }

    const skills = async () => {
        return await fetch('http://localhost:8000/api/skills/').then(res => res.json())
    }

    return {
        experiences: experiences(),
        skills: skills()
    }
}
