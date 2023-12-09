import { SERVEUR_URL } from '$env/static/private'
export const load = () => {
    const experiences = async () => {
        return await fetch(`${SERVEUR_URL}/api/experiences/`).then(res => res.json())
    }

    const skills = async () => {
        return await fetch(`${SERVEUR_URL}/api/categories/`).then(res => res.json())
    }

    return {
        experiences: experiences(),
        skills: skills(),
    }
}
