import type { PageServerLoad, Actions } from './$types';
import { SERVEUR_URL } from '$env/static/private'

export const load: PageServerLoad = () => {
    const skills = async () => {
        return await fetch(`${SERVEUR_URL}/api/skills/`).then(res => res.json())
    }

    return {
        skills: skills()
    }
}


export const actions: Actions = {
    create_project: async ({ request }) => {
        const formData = await request.formData();
        
        await fetch(`${SERVEUR_URL}/api/projects/`, {
            method: 'POST',
            body: formData
        })

        return { success: true };
    }

}