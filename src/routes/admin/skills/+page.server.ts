import type { PageServerLoad, Actions } from './$types';
import { SERVEUR_URL } from '$env/static/private'
import { writeFile } from 'fs/promises';


export const load: PageServerLoad = () => {
    const skills = async () => {
        return await fetch(`${SERVEUR_URL}/api/skills/`).then(res => res.json())
    }

    return {
        skills: skills()
    }
}