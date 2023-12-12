import { SERVEUR_URL } from '$env/static/private'
export const load = async () => {
    const [experiencesData, skillsData, projectsData] = await Promise.all([
        fetch(`${SERVEUR_URL}/api/experiences/`).then(res => res.json()),
        fetch(`${SERVEUR_URL}/api/categories/`).then(res => res.json()),
        fetch(`${SERVEUR_URL}/api/projects/`).then(res => res.json())
    ]);

    return {
        experiences: experiencesData,
        skills: skillsData,
        projects: projectsData
    };
}


